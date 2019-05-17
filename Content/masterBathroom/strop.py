import eng

class Strop:
	name = 'strop'
	#type = 'Item'
	visible = False 
	aliases = []
	descriptions = {'desc': "It's a strop, a long leather strap used for sharpening razor blades.",
					'takeStrop': "You pick up the strop.",
					'alreadyTakenStrop': "You already took that.",
					'touchStrop': "You touch the strop. There's no achievement for this.",
					'eatStrop': "Though the strop is leather, it has very little nutritional value.",
					'dropNoHold': "You pick up the strop and then put it back. A great sense of accomplishment washes over you.",
					'dropStrop': "You put down the strop. It's here if you need it later."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		if eng.inInventory(self):
			return self.descriptions['alreadyTakenStrop']
		else:
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['takeStrop']


	def touch(self):
		return self.descriptions['touchStrop']


	def drop(self):
		if eng.inInventory(self) == False:
			return self.descriptions['dropNoHold']
		else:
			eng.removeFromInventory(self)
			eng.dropItem(self)
			return self.descriptions['dropStrop']


	def eat(self, otherThing):
		return self.descriptions['eatStrop']
			

strop = Strop()
eng.setupItem(strop)