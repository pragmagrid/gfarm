#!/bin/bash
vmbasedir=$1
mv  $vmbasedir/etc/yum.conf $vmbasedir/etc/yum.conf.vm
cp /etc/yum.conf $vmbasedir/yum.conf
yum --installroot=$vmbasedir install ec2-ami-tools ec2-api-tools ruby ruby-docs ruby-libs rsync
cat > $vmbasedir/etc/sysconfig/network-scripts/ifcfg-eth0 << 'EOF'
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
EOF
cat > $vmbasedir/etc/sysconfig/network << 'EOF'
NETWORKING=yes
EOF
cat > $vmbasedir/etc/resolv.conf << 'EOF'
search sdsc.edu
EOF

cd $vmbasedir/tmp
wget http://10.1.1.1/ec2/ec2-modules-2.6.18-xenU-ec2-v1.2-x86_64.tgz
cd $vmbasedir/
tar xzf $vmbasedir/tmp/ec2-modules-2.6.18-xenU-ec2-v1.2-x86_64.tgz

cat > $vmbasedir/tmp/remake.initrd << 'EOF'
#!/bin/bash
mkinitrd --builtin=ehci-hcd --builtin=ohci-hcd --builtin=uhci-hcd --builtin=xenblk --builtin=xennet --omit-scsi-modules /boot/initrd-2.6.18-xenU-ec2-v1.2  2.6.18-xenU-ec2-v1.2
EOF
chmod +x $vmbasedir/tmp/remake.initrd
chroot $vmbasedir /tmp/remake.initrd

cat > $vmbasedir/boot/grub/grub.conf << 'EOF'
default=0
timeout=5
hiddenmenu
title EC2 (vmlinuz-2.6.18-xenU-ec2-v1.2)
        root (hd0,0)
        kernel /boot/vmlinuz-2.6.18-xenU-ec2-v1.2  ro root=LABEL=/ rhgb quiet
        initrd /boot/initrd-2.6.18-xenU-ec2-v1.2
EOF

##
## Startup Script to copy ssh key 
##
touch $vmbasedir/etc/rc.d/init.d/ec2-root-ssh
chmod 755 $vmbasedir/etc/rc.d/init.d/ec2-root-ssh
cat > $vmbasedir/etc/rc.d/init.d/ec2-root-ssh << 'EOF'
#!/bin/sh
# $Id$
#
# chkconfig: 2345 99 40
# description: ec2 ssh key access
#
. /etc/rc.d/init.d/functions

RETVAL=0

copykeys() {
if [ ! -d /root/.ssh ] ; then
        mkdir -p /root/.ssh
        chmod 700 /root/.ssh
fi
# Fetch public key using HTTP
curl http://169.254.169.254/2009-04-04//meta-data/public-keys/0/openssh-key > /tmp/my-key  2>/dev/null
if [ $? -eq 0 ] ; then
	cat /tmp/my-key >> /root/.ssh/authorized_keys
	chmod 700 /root/.ssh/authorized_keys
	rm /tmp/my-key
   	return 0
else
	return -1
fi
}

case "$1" in
   start)
	echo -n "Adding User-Supplied EC2 Root SSH Key"
	copykeys 
	RETVAL=$?
	echo
	[ $RETVAL -eq 0 ] 
	;;

  stop)
      echo -n "EC2 Root SSH Key "
	[ $RETVAL -eq 0 ]
	;;

  restart|reload)
   	$0 stop
   	$0 start
   	RETVAL=$?
	;;
  *)
	echo "Usage: $0 {start|stop|restart}"
	exit 1
esac

exit $RETVAL

EOF

chroot $vmbasedir  chkconfig --add ec2-root-ssh

if [ ! -d $vmbasedir/mnt/ec2image ]; then
	mkdir -p $vmbasedir/mnt/ec2image
fi

##
## Startup Script to Modify Condor Configuration 
##
touch $vmbasedir/etc/rc.d/init.d/ec2-condor-collector
chmod 755 $vmbasedir/etc/rc.d/init.d/ec2-condor-collector
cat > $vmbasedir/etc/rc.d/init.d/ec2-condor-collector << 'EOF'
#!/bin/sh
# $Id$
#
# chkconfig: 2345 29 40
# description: EC2 Condor Pool Extension
#
# interprets user-supplied instance data of the form
# condor:<name of collector>:lowport:highport
# eg. ec2-run-instances  -d "condor:landphil.rocksclusters.org:40000:40050"
#      will cause condor client to report to collector and use ports 40000 - 40050
. /etc/rc.d/init.d/functions

RETVAL=0

set_condor_collector() {
# Fetch metadata information 
publicIP=`curl http://instance-data.ec2.internal/latest/meta-data/public-ipv4 2>/dev/null`
publicHostname=`curl http://instance-data.ec2.internal/latest/meta-data/public-hostname 2>/dev/null`
privateIP=`curl http://instance-data.ec2.internal/latest/meta-data/local-ipv4 2>/dev/null`
privateHostname=`curl http://instance-data.ec2.internal/latest/meta-data/local-hostname 2>/dev/null`
instanceData=`curl http://instance-data.ec2.internal/latest/user-data 2>/dev/null`
#
# Example instance data
# instanceData="condor:landphil.rocksclusters.org:40000:40050"
#
condorData=`echo $instanceData | grep "condor" `
if [ "x$condorData" != "x" ]; then
	/bin/hostname $publicHostname
	collector=`echo $condorData | awk -F: '{print $2}'`
	lowport=`echo $condorData | awk -F: '{print $3}'`
	highport=`echo $condorData | awk -F: '{print $4}'`
	privateDomain=`echo $privateHostname | cut -d . -f 2-`
	publicDomain=`echo $publicHostname | cut -d . -f 2-`

	condorLocal=/etc/condor/condor_config.local

	if  ["x$lowport" != "x" ]; then
		echo "LOWPORT = $lowport" >> $condorLocal
	fi
	if  ["x$highport" != "x" ]; then
		echo "HIGHPORT = $highport" >> $condorLocal
	fi
	if  ["x$collector" != "x" ]; then
		echo "COLLECTOR_HOST = $collector" >> $condorLocal
	fi
	echo "COLLECTOR_SOCKET_CACHE_SIZE=1000" >> $condorLocal
	echo "UPDATE_COLLECTOR_WITH_TCP=True" >> $condorLocal
	echo "HOSTALLOW_WRITE = $collector,*.$privateDomain" >> $condorLocal
	echo "ALLOW_WRITE = \$(HOSTALLOW_WRITE)" >> $condorLocal
	echo "PRIVATE_NETWORK_NAME = $privateDomain" >> $condorLocal 
	echo "TCP_FORWARDING_HOST = $publicIP" >> $condorLocal 
	echo "PRIVATE_NETWORK_INTERFACE = $privateIP" >> $condorLocal 
	echo "NETWORK_INTERFACE = $privateIP" >> $condorLocal 
fi
}
case "$1" in
   start)
	echo -n "Setting Up Remote Condor Collector"
	set_condor_collector
	RETVAL=$?
	echo
	[ $RETVAL -eq 0 ] 
	;;

  stop)
      echo -n "Remote Condor Collector "
	[ $RETVAL -eq 0 ]
	;;

  restart|reload)
   	$0 stop
   	$0 start
   	RETVAL=$?
	;;
  *)
	echo "Usage: $0 {start|stop|restart}"
	exit 1
esac

exit $RETVAL

EOF

chroot $vmbasedir  chkconfig --add ec2-condor-collector
