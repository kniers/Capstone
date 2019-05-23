import eng

class TopDrawer:
	name = 'top drawer'
	#type = 'Item'
	visible = False 
	aliases = []
	descriptions = {'closedDesc': "It's the top drawer of the filing cabinet. It's identical in appearance to the bottom drawer.",
					'takeOnMe': "It's attached to the filing cabinet.",
					'touchMe': "That's very touching of you.",
					'eatMe': "The drawer is brown, but it's not made out of chocolate.",
					'openMe': "You open the drawer."}
	properties = {'opened': False}
	
	
	def look(self):
		self.visible = True
		if self.properties['opened']:
			return self.descriptions['openDesc']
		else:
			return self.descriptions['closedDesc']


	# FIXME: Change this if something is put in the drawer later
	def open(self):
		return self.descriptions['openMe']
	
	
	def take(self):
		return self.descriptions['takeOnMe']


	def touch(self):
		return self.descriptions['touchMe']


	def eat(self):
		return self.descriptions['eatMe']
			

topDrawer = TopDrawer()
eng.setupItem(topDrawer)
