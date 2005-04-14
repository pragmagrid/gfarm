# $Id$
#
# @Copyright@
# @Copyright@
#
# $Log$
# Revision 1.1  2005/04/14 16:09:20  mjk
# *** empty log message ***
#

COPYRIGHT.FILE = $(shell pwd)/COPYRIGHT

ROLLSROOT = ..
-include $(ROLLSROOT)/etc/Rolls.mk
include Rolls.mk

default: roll
