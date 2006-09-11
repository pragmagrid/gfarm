#! /opt/rocks/bin/python
#
# $RCSfile$
#
# @Copyright@
# 
# 				Rocks
# 		         www.rocksclusters.org
# 		        version 4.2.1 (Cydonia)
# 
# Copyright (c) 2006 The Regents of the University of California. All
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
# notice unmodified and in its entirety, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided 
# with the distribution.
# 
# 3. All advertising and press materials, printed or electronic, mentioning
# features or use of this software must display the following acknowledgement: 
# 
# 	"This product includes software developed by the Rocks 
# 	Cluster Group at the San Diego Supercomputer Center at the
# 	University of California, San Diego and its contributors."
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
# Revision 1.7  2006/09/11 22:48:39  mjk
# monkey face copyright
#
# Revision 1.6  2006/08/10 00:10:45  mjk
# 4.2 copyright
#
# Revision 1.5  2006/01/16 06:49:08  mjk
# fix python path for source built foundation python
#
# Revision 1.4  2005/10/12 18:09:30  mjk
# final copyright for 4.1
#
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


