#
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
# Revision 1.4  2005/04/15 00:39:13  mjk
# *** empty log message ***
#

SELFCONTAINED = 1
COPYRIGHT.FILE = $(shell pwd)/COPYRIGHT
ROLLSROOT = ..
-include $(ROLLSROOT)/etc/Rolls.mk
include Rolls.mk

default: roll
