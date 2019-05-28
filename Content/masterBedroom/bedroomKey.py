import eng

class BedroomKey:
	name = 'bedroom key'
	#type = 'Item'
	visible = False 
	aliases = ['key']
	descriptions = {'desc': "This is a pretty standard key in terms of appearance.",
					'dropNoHold': "You can't drop the key, you aren't holding it!", 
					'drop': "You dropped the key back into the nightstand where you found it. Don't want to place it anywhere else and raise suspicion.", 
					'alreadyTakenKey': "You're already carrying the key.", 
					'takeKey': "You've picked up the key. Who knows what door you'll need it for, but it'll probably be useful."}
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
	

	def drop(self):
		if eng.inInventory(self) == False:
			return self.descriptions['dropNoHold']
		else:
			eng.removeFromInventory(self)
			eng.dropItem(self)
			return self.descriptions['drop']


key = BedroomKey()
eng.setupItem(key)