# 
# $Id$
#
# @Copyright@
# 
# 				Rocks
# 		         www.rocksclusters.org
# 		           version 4.1 (fuji)
# 
# Copyright (c) 2005 The Regents of the University of California. All
# rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# 
# 3. All advertising materials mentioning features or use of this
# software must display the following acknowledgement: 
# 
# 	"This product includes software developed by the Rocks 
# 	Cluster Group at the San Diego Supercomputer Center and
# 	its contributors."
# 
# 4. Neither the name or logo of this software nor the names of its
# authors may be used to endorse or promote products derived from this
# software without specific prior written permission.  The name of the
# software includes the following terms, and any derivatives thereof:
# "Rocks", "Rocks Clusters", and "Avalanche Installer".
# 
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# @Copyright@
#
# $Log$
# Revision 1.1.2.2  2007/08/23 09:09:46  nadya
# get the name right
#
# Revision 1.1.2.1  2007/08/17 22:01:30  nadya
# add fuse src rpm to the roll for a rebuild during first boot.
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


