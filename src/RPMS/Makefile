# $Id$
#
# @Copyright@
# @Copyright@
#
# $Log$
# Revision 1.1.4.1  2007/09/19 10:14:28  nadya
# bring from 4.2.1
#
#

REDHAT.ROOT     = $(PWD)/../../
ROCKSROOT       = ../../../../..
MAKE.iscontrib  = 1
-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

PACKAGES=$(wildcard *.$(ARCH).rpm)

rpm::
	cp $(PACKAGES) $(REDHAT.RPMS)/$(ARCH)/ || true

