#! /opt/rocks/usr/bin/python
#
# $RCSfile$
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
# Revision 1.4.4.2  2007/08/27 20:41:33  nadya
# add Gfarm in Component name
#
# Revision 1.4.4.1  2007/08/13 20:26:16  nadya
# bring from 4.3
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
			'service="Info" and component="GfarmAgent"')
		agentServer = self.fetchone()

		self.execute('select value from app_globals where '
			'service="Info" and component="GfarmMetaServer"')
		metaServer = self.fetchone()
		pgsqlServer = metaServer

		print 'spool /state/partition1/gfarm'
		print 'spool_serverport 600'
		print 'metadb_serverhost %s' % metaServer
		print 'metadb_serverport 601'
		print 'postgresql_serverhost %s' % pgsqlServer
		print 'postgresql_serverport 10602'
		print 'postgresql_dbname gfarm'
		print 'postgresql_user gfarm'
		print 'auth disable sharedsecret *'
		print 'auth enable gsi_auth *'
		print 'auth enable gsi *'
		if agentServer is not None:
			print 'agent_serverhost %s' % agentServer
			print 'agent_serverport 603'

