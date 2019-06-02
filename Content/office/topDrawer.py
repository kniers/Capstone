import eng

class TopDrawer:
	name = 'top drawer'
	#type = 'Item'
	visible = False 
	aliases = []
	descriptions = {'closedDesc': "It's the top drawer of the filing cabinet. It's identical in appearance to the bottom drawer for the most part.",
					'openDescHit': "You look inside the drawer. Bingo! There are some papers here. They must be important.",
					'openDescMiss': "You look inside the drawer. There's a small gold statue in there. It's not what you're here for, but it's a good consolation prize.",
					'takeOnMe': "It's attached to the filing cabinet.",
					'touchMe': "That's very touching of you.",
					'eatMe': "The drawer is brown, but it's not made out of chocolate.",
					'openLocked': "You try the drawer, but it's locked.",
					'openMe': "The key fits perfectly. You open the drawer. ",
					'openBad': "You try to stuff it in the keyhole, but it doesn't work.",
					'alreadyOpen': "You already opened that."}
	properties = {'opened': False, 'locked': True}
	
	
	def look(self):
		self.visible = True
		if self.properties['opened']:
			currRoom = eng.getCurrentRoom()
			if 'secret plans' in currRoom.items:
				return self.descriptions['openDescHit']
			elif 'gold statue' in currRoom.items:
				return self.descriptions['openDescMiss']
			else:
				return "It's empty."
		else:
			return self.descriptions['closedDesc']


	def open(self, key):
		if self.properties['opened']:
			return self.descriptions['alreadyOpen']
		if key is None:
			return self.descriptions['openLocked']
		elif key.name == 'strange key':
			self.properties['opened'] = True
			self.properties['locked'] = False
			currRoom = eng.getCurrentRoom()
			meesa = eng.getItemByName("self")
			meesa.properties['placesOpened'] = meesa.properties['placesOpened'] + 1
			if meesa.properties['placesOpened'] == 3:
				sp = eng.getItemByName('secret plans')
				currRoom = eng.getCurrentRoom()
				currRoom.items.append('secret plans')
				currRoom.items.remove('gold statue')
			else:
				gs = eng.getItemByName('gold statue')
				gs.visible = True
			return self.descriptions['openMe'] + self.look()
		else:
			return self.descriptions['openBad']
	
	
	def take(self):
		return self.descriptions['takeOnMe']


	def touch(self):
		return self.descriptions['touchMe']


	def eat(self):
		return self.descriptions['eatMe']
			

topDrawer = TopDrawer()
eng.setupItem(topDrawer)
