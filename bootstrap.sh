#!/bin/sh
#
# $Id$
#
# @Copyright@
# @Copyright@
#
# $Log$
# Revision 1.1.4.3  2007/09/21 08:36:58  nadya
# specify needed rpms by name
#
# Revision 1.1.4.2  2007/09/19 11:43:37  nadya
# force order installing rpms
#
# Revision 1.1.4.1  2007/09/19 10:14:27  nadya
# bring from 4.2.1
#
#
#
. ../etc/bootstrap-functions.sh

compile RPMS
install_os_packages gfarm-base
install globus-gpt
install globus-gssapi-gsi-gcc32
install globus-proxy-utils-gcc32
install postgres
install postgres-libs
install postgres-devel

compile SRPMS
install fuse
install fuse-devel
install fuse-libs
install gfarm-libs
install gfarm-client
install gfarm-devel

