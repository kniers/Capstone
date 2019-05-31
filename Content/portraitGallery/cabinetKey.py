import eng

class CabinetKey:
	name = 'strange key'
	#type = 'Item'
	visible = False 
	aliases = ['key']
	descriptions = {'desc': "It's a small key. It's too small for a door; it looks like it might go to a filing cabinet.",
					'takeKey': "You take the key.",
					'alreadyTakenKey': "You already took that.",
					'touchKey': "You touch the key. That's about it.",
					'eatKey': "munch",
					'dropNoHold': "You pick up the key, but change your mind and put it back down.",
					'drop': "You put down the key in a place where you'll (hopefully) remember it."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		if eng.inInventory(self):
			return self.descriptions['alreadyTakenKey']
		else:
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['takeKey']


	def touch(self):
		return self.descriptions['touchKey']


	def drop(self):
		if eng.inInventory(self) == False:
			return self.descriptions['dropNoHold']
		else:
			eng.removeFromInventory(self)
			eng.dropItem(self)
			return self.descriptions['drop']


	def eat(self):
		return self.descriptions['eatKey']
			

cabinetKey = CabinetKey()
eng.setupItem(cabinetKey)
