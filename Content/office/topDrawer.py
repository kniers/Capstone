import eng

class TopDrawer:
	name = 'top drawer'
	#type = 'Item'
	visible = False 
	aliases = ['drawer']
	descriptions = {'closedDesc': "It's the top drawer of the filing cabinet. It's identical in appearance to the bottom drawer for the most part.",
					'openDescHit': "You look inside the drawer. Bingo! There's what you're looking for! Now you just have to take it and exit the front door.",
					'openDescMiss': "You look inside the drawer. There's a small gold statue in there. It's not what you're here for, but it's a good consolation prize.",
					'takeOnMe': "It's attached to the filing cabinet.",
					'touchMe': "That's very touching of you.",
					'eatMe': "The drawer is brown, but it's not made out of chocolate.",
					'openLocked': "You try the drawer, but it's locked.",
					'openMe': "The key fits perfectly. You open the drawer.",
					'openBad': "You try to stuff it in the keyhole, but it doesn't work.",
					'alreadyOpen': "You already opened that."}
	properties = {'opened': False, 'locked': True}
	
	
	def look(self):
		self.visible = True
		if self.properties['opened']:
			meesa = eng.getItemByName("self")
			meesa.properties['placesOpened'] = meesa.properties['placesOpened'] + 1
			if meesa.properties['placesOpened'] == 3:
				sp = eng.getItemByName('secret plans')
				currRoom = eng.getCurrentRoom()
				currRoom.items.add('secret plans')
				return self.descriptions['openDescHit']
			else:
				gs = eng.getItemByName('gold statue')
				gs.visible = True
				return self.descriptions['openDescMiss']
		else:
			return self.descriptions['closedDesc']


	def open(self, kee):
		if self.properties['opened']
			return self.descriptions['alreadyOpen']
		if kee is None:
			return self.descriptions['openLocked']
		elif kee.name == 'strange key':
			self.properties['opened'] = True
			self.properties['locked'] = False
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
