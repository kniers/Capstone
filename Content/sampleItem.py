import eng

class SampleItem:
	name = 'sample item'
	#type = 'Item'
	visible = False 
	aliases = []
	descriptions = {'desc': "This is a sample item. It doesn't do anything.",
					'takeSI': "AAAAAHHH",
					'alreadyTakenSI': "You already took that.",
					'touchSI': "boop",
					'eatSuccessSI': "munch",
					'eatFailSI': "urp",
					'dropNoHold': "huh?",
					'drop': "crash"}
	properties = {'sample': True}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		if eng.inInventory(self):
			return self.descriptions['alreadyTakenSI']
		else:
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['takeSI']


	def touch(self):
		return self.descriptions['touchSI']


	def drop(self):
		if eng.inInventory(self) == False:
			return self.descriptions['dropNoHold']
		else:
			eng.removeFromInventory(self)
			currRoom = eng.getCurrentRoom()
			currRoom.addItem('letter opener')
			return self.descriptions['drop']


	def eat(self, otherThing):
		if otherThing is None:
			return self.descriptions['eatFailSI']
		else
			self.sharp = True
			return self.descriptions['eatSuccessSI']
			

sampleItem = SampleItem()
eng.setupItem(sampleItem)