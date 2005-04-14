# --------------------------------------------------- -*- Makefile -*- --
# $Id$
#
# @Copyright@
# @Copyright@
#
# $Log$
# Revision 1.1  2005/04/14 13:29:41  mjk
# *** empty log message ***
#

REDHAT.ROOT = $(PWD)/../../
ROCKSROOT = ../../../../..
-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

install::
	mkdir -p $(ROOT)/etc/profile.d
	install -m744 etc/profile.d/*.sh	$(ROOT)/etc/profile.d/
	install -m744 etc/profile.d/*.csh	$(ROOT)/etc/profile.d/

build: $(SCRIPTS)

clean::
	-rm -f $(SCRIPTS)

