#! /usr/bin/env python
#
# $RCSfile$
#
# @Copyright@
# @Copyright@
#
# $Log$
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


