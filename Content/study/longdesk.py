import eng

class Longdesk:
	name = 'longDesk'
	#type = 'Item'
	visible = True 
	aliases = ['desk', 'long desk', 'drawer']
	descriptions = {'LongDeskDesc': "There is a long walnut desk along the wall that seats three. Looks to be a great place to read or study. There is a drawer on the left side of the desk. ",
					'openedDesc': "The drawer is lined in red velvet. ",
					'bibleDesc': "In the drawer is a beautiful, leather-bound bible with pure gold enlaid cross on the cover. The cross has seven half-carat diamonds along the center.",
					'nothingDesc': ", but nothing inside. ",
					'alreadyOpenDesc': "The drawer is already open. Are you trying to break the desk? "}
	properties = {'openedDrawer': False}

	def look(self):
		if self.properties['openedDrawer'] == True:
			desc = self.descriptions['openedDesc']
			currRoom = eng.getCurrentRoom()
			if 'Bible' in currRoom.items:
				return desc + self.descriptions['bibleDesc']
			else:
				return desc + self.descriptions['nothingDesc']
		else:
			return self.descriptions['LongDeskDesc']	

	def open(self):
		if self.properties['openedDrawer'] == True:
			return self.descriptions['alreadyOpenDesc']
		else:
			self.properties['openedDrawer'] = True
			currRoom = eng.getCurrentRoom()
			bible = eng.getItemByName('Bible')
			if bible is not None:
				bible.visible = True				
			return self.look()	

longdesk = Longdesk()
eng.setupItem(longdesk)
