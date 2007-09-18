#!/bin/sh
#
# $Id$
#
# @Copyright@
# @Copyright@
#
# $Log$
# Revision 1.1.2.1  2007/09/18 12:24:45  nadya
# initial revision
#
#
. ../etc/bootstrap-functions.sh

compile RPMS
install globus-gpt
install globus-proxy-utils-gcc32
install globus-gssapi-gsi-gcc32

install_os_packages gfarm-base

