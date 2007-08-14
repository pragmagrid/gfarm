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
		fqdn = self.metaserver.value()
		domains = fqdn.split('.')
		if len(domains) > 2:
			org = domains[-2]
			name = domains[0]

	def valCb(self, field):
		if string.capitalize(field.value()) == 'None':
			field.set('None')

	def __call__(self, screen, Info):
		self.screen = screen
		retval = INSTALL_OK

		default = "pine.hpcc.jp"
		self.metaserver = Entry(24, default)
		self.metaserver.setCallback(self.nameCb)

		default = "cluster.hpc.org"
		self.agent = Entry(24, default)
		self.agent.setCallback(self.valCb, (self.agent))

		default = "cluster.hpc.org"
		self.fsnode = Entry(24, default)
		self.fsnode.setCallback(self.valCb, (self.fsnode))

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

		leftGrid.setField(self.label("Gfarm Agent:"), x, y, anchorLeft = 1)
		y += 1
		leftGrid.setField(self.agent, x, y, anchorLeft = 1)
		y += 1

		leftGrid.setField(self.label("Gfarm FS Node:"), x, y, anchorLeft = 1)
		y += 1
		leftGrid.setField(self.fsnode, x, y, anchorLeft = 1)
		y += 1

		infoGrid.setField(leftGrid, 0,0, anchorLeft=1, anchorTop=1)
		infoGrid.setField(rightGrid, 1,0, (2,0,0,0), anchorLeft=1, anchorTop=1)

		toplevel.add(infoGrid, 0, 1, anchorTop=1)
		toplevel.add(bb, 0, 2, growx=0)

		done = 0
		while not done:
			fieldlabel = ''

			result = toplevel.run()

			rc = bb.buttonPressed(result)
			if rc == "back":
				retval = INSTALL_BACK
				done = 1
				continue

			Info.Metaserver = self.metaserver.value()
			Info.Agent = self.agent.value()
			Info.FSNode = self.fsnode.value()

			if Info.Agent == 'cluster.hpc.org':
				fieldlabel = _("Gfarm Agent")
			elif Info.FSNode == 'cluster.hpc.org':
				fieldlabel = _("Gfarm FS Node")
			else:
				done = 1

			if done == 0:
				ButtonChoiceWindow(screen, "",
					(_("You must supply a value for the\n"
						"'%s' or use NONE") % (fieldlabel)),
				buttons = [ TEXT_OK_BUTTON ], width = 50)

		screen.popWindow()
		return retval


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
