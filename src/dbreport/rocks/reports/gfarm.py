#! /opt/rocks/usr/bin/python
#
# $RCSfile$
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
# Revision 1.3  2005/08/08 21:24:58  mjk
# foundation
#
# Revision 1.2  2005/04/14 14:04:31  mjk
# *** empty log message ***
#
# Revision 1.1  2005/04/14 14:04:13  mjk
# *** empty log message ***
#

import os
import socket
import string
import rocks.reports.base


class Report(rocks.reports.base.ReportBase):

	def run(self):
		self.execute('select value from app_globals where '
			'service="Kickstart" and component="PrivateHostname"')
		metaServer = self.fetchone()
		ldapServer = metaServer

		print 'spool /state/partition1/gfarm'
		print 'metadb_serverhost %s' % metaServer
		print 'ldap_serverhosts %s' % ldapServer
		print 'ldap_serverport 389'
		print 'ldap_base_dn "dc=example, dc=com"'
		print 'auth disable sharedsecret *'
		print 'auth enable gsi *'


