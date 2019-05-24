import eng

class BottomDrawer:
	name = 'bottom drawer'
	#type = 'Item'
	visible = False 
	aliases = ['drawer']
	descriptions = {'closedDesc': "It's the bottom drawer of the filing cabinet. It's identical in appearance to the top drawer. for the most part.",
					'fullDesc': " The blueprints are still inside.",
					'emptyDesc': " The drawer is empty.",
					'takeOnMe': "It's attached to the filing cabinet.",
					'touchMe': "That's very touching of you.",
					'eatMe': "The drawer is brown, but it's not made out of chocolate.",
					'openMe': "You open the drawer. There's a roll of blueprints inside.",
					'alreadyOpened': "You already did that."}
	properties = {'opened': False}
	
	
	def look(self):
		self.visible = True
		if self.properties['opened']:
			currRoom = eng.getCurrentRoom()
			if 'blueprints' in currRoom.items:
				return self.descriptions['closedDesc'] + self.descriptions['fullDesc']
			else:
				return self.descriptions['closedDesc'] + self.descriptions['emptyDesc']
		else:
			return self.descriptions['closedDesc']


	def open(self):
		if self.properties['opened']:
			return self.descriptions['alreadyOpened']
		else:
			blueprints = eng.getItemByName('blueprints')
			if blueprints is not None:
				blueprints.visible = True
			return self.descriptions['openMe']
	
	
	def take(self):
		return self.descriptions['takeOnMe']


	def touch(self):
		return self.descriptions['touchMe']


	def eat(self):
		return self.descriptions['eatMe']
			

bottomDrawer = BottomDrawer()
eng.setupItem(bottomDrawer)
