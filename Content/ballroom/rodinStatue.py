import eng

class RodinStatue:
	name = 'rodin statue'
	#type = 'Item'
	visible = True
	aliases = ['statue']
	descriptions = {'desc': "It's a life-sized human statue by the artist Rodin. Rodin? He's the guy who sculpted The Thinker. There's somebody in the mansion who would like to see this."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		rl = eng.getItemByName('rodin location')
		rl.visible = True
		eng.addToInventory(rl)
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


rodinStatue = RodinStatue()
eng.setupItem(rodinStatue)
