# $Id$
#
# @Copyright@
# Copyright (c) 2003, 2004, 2005 National Institute of Advanced
# Industrial Science and Technology (AIST).  All Rights Reserved.
# 
# The authors hereby grant permission to use, copy, modify, and
# distribute this software and its documentation for any purpose,
# provided that existing copyright notices are retained in all copies
# and that this notice is included verbatim in any distributions.  The
# name of AIST may not be used to endorse or promote products derived
# from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE AUTHORS ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED.  IN NO EVENT SHALL THE AUTHORS OR DISTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, ITS
# DOCUMENTATION, OR ANY DERIVATIVES THEREOF, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# @Copyright@
#
# $Log$
# Revision 1.3  2005/04/14 16:23:01  mjk
# *** empty log message ***
#
# Revision 1.2  2005/04/14 16:09:38  mjk
# *** empty log message ***
#
# Revision 1.1  2005/04/14 16:05:59  mjk
# *** empty log message ***
#
# Revision 1.2  2004/09/01 19:11:55  mjk
# *** empty log message ***
#
# Revision 1.1  2004/01/15 00:45:17  mjk
# *** empty log message ***
#

MAKE.iscontrib = 1
REDHAT.ROOT = $(PWD)/../../
ROCKSROOT = ../../../../..
-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

rpm::
	rpmbuild --rebuild --nodeps *.src.rpm
	cp /usr/src/redhat/RPMS/$(ARCH)/gfarm*.rpm ../../RPMS/$(ARCH)/


