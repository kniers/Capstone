import eng

class RodinLocation:
	name = 'rodin location'
	#type = 'Item'
	visible = False
	aliases = ['rodin clue']
	descriptions = {'desc': "You found a statue by Rodin. You can tell people about where it is if they're interested."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	#def take(self):
	#	if eng.inInventory(self):
	#		return self.descriptions['alreadyTakenSI']
	#	else:
	#		eng.addToInventory(self) # adds to inventory and removes from current room 
	#		return self.descriptions['takeSI']


	#def touch(self):
	#	return self.descriptions['touchSI']


	#def drop(self):
	#	if eng.inInventory(self) == False:
	#		return self.descriptions['dropNoHold']
	#	else:
	#		eng.removeFromInventory(self)
	#		eng.dropItem(self)
	#		return self.descriptions['drop']


	#def eat(self, otherThing):
	#	if otherThing is None:
	#		return self.descriptions['eatFailSI']
	#	else:
	#		self.sharp = True
	#		return self.descriptions['eatSuccessSI']


rodinLocation = RodinLocation()
eng.setupItem(rodinLocation)
