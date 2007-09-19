# 
# $Id$
#
# @Copyright@
# @Copyright@
#
# $Log$
# Revision 1.1.4.1  2007/09/19 10:14:29  nadya
# bring from 4.2.1
#
#

REDHAT.ROOT	= $(PWD)/../../
ROCKSROOT	= ../../../../..

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk


version.mk: version.mk.in
	/bin/cat version.mk.in ..//SRPMS/version.mk > version.mk

install::
	mkdir -p $(RPM_BUILD_ROOT)/opt/rocks/SRPMS
	rm -f $(REDHAT.SRPMS)/gfarm-config*src.rpm 
	cp $(REDHAT.ROOT)/src/SRPMS/$(FUSE)-$(FUSE_VERSION).src.rpm $(RPM_BUILD_ROOT)/opt/rocks/SRPMS

clean::
	rm -r version.mk


