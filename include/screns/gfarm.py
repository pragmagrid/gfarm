#
# $Id$
#
# Gfarm screen 
#

class GFarmInfoWindow:

	def label(self, name, help=None):
		if not help:
			return Label(_(name))

		table = Grid(2,1)
		table.setField(Label(_(name)), 0,0, anchorLeft=1)
		table.setField(Label(_(help)), 1,0, (2,0,0,0), anchorLeft=1)
		return table


	def nameCb(self):
		fqdn = self.fqdn.value()
		#self.contact.set('admin@%s' % fqdn)
		#self.url.set('http://%s/' % fqdn)
		domains = fqdn.split('.')
		if len(domains) > 2:
			org = domains[-2]
			name = domains[0]
			#self.org.set(org.capitalize())
			#self.name.set(name.capitalize())


	def __call__(self, screen, Info):

		default = "pine.hpcc.jp"
		self.metaserver = Entry(24)
		self.metaserver.set(default)

		default = ""
		self.agent = Entry(24)
		self.agent.set(default)

		default = ""
		self.fsnode = Entry(24)
		self.fsnode.set(default)

		bb = ButtonBar (screen, (TEXT_OK_BUTTON, ("Back","back")))
		toplevel = GridFormHelp (screen, _("Gfarm Setup Information"), "", 1, 3)
		leftGrid = Grid(1,12)
		rightGrid = Grid(1,12)
		infoGrid = Grid(2,1)

		toplevel.add(self.label("Information Used to Configure GFarm"), 
			0, 0, (0,0,0,1))

		# Left column
		x, y = (0, 0)
		
		leftGrid.setField(self.label("Gfarm Metaserver:"), x, y, anchorLeft = 1)
		y += 1
		leftGrid.setField(self.metaserver, x, y, anchorLeft = 1)
		y += 1

		leftGrid.setField(self.label("Gfarm FS Node:"), x, y, anchorLeft = 1)
		y += 1
		leftGrid.setField(self.fsnode, x, y, anchorLeft = 1)
		y += 1

		infoGrid.setField(leftGrid, 0,0, anchorLeft=1, anchorTop=1)
		infoGrid.setField(rightGrid, 1,0, (2,0,0,0), anchorLeft=1, anchorTop=1)

		toplevel.add(infoGrid, 0, 1, anchorTop=1)
		toplevel.add(bb, 0, 2, growx=0)

		result = toplevel.runOnce()

		Info.Metaserver = self.metaserver.value()
		Info.Agent = self.agent.value()
		Info.FSNode = self.fsnode.value()

		rc = bb.buttonPressed(result)

		if rc == "back":
			return INSTALL_BACK

		return INSTALL_OK



if __name__ == '__main__':
	from snack import *

	class Info: pass
	def _(str): return str

	TRUE			= 1
	FALSE			= 0
	INSTALL_OK		= 0
	INSTALL_BACK		= -1
	INSTALL_NOOP		= -2
	TEXT_F12_CHECK		= "F12"
	TEXT_OK_BUTTON		= ( "OK",	"ok" )
	TEXT_CANCEL_BUTTON	= ( "Cancel",	"cancel" )
	TEXT_BACK_BUTTON	= ( "Back",	"back" )
	TEXT_YES_BUTTON		= ( "Yes",	"yes" )
	TEXT_NO_BUTTON		= ( "No",	"no" )

	screen = SnackScreen()
	info = Info()
 	o = GFarmInfoWindow()
	o(screen, info)
	screen.finish()
	print info.__dict__

else:
	addScreen("GFarmInfoWindow")
