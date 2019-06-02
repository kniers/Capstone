import eng

class SpareKey:
	name = 'spare key'
	#type = 'Item'
	visible = False 
	aliases = ['key']
	descriptions = {'desc': "This is a pretty standard key in terms of appearance.",
					'dropNoHold': "You can't drop the key, you aren't holding it!", 
					'drop': "You set the spare key down. It'll be here in case you need it again.", 
					'alreadyTakenKey': "You're already carrying the key.", 
					'takeKey': "You've picked up the key. Something tells you that it will come in handy very soon."}
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
			eng.dropItem(self)
			return self.descriptions['drop']

	def use(self, other):
		if eng.inInventory(self):
			if other is None:
				return "Use it on what?"
			elif other.name == 'masterBedDoor':
				return other.open(self)
			else:
				return "That didn't work"
		else:
			return "You don't have it. Try taking it."

key = SpareKey()
eng.setupItem(key)