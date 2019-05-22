import eng

class Blueprints:
	name = 'blueprints'
	#type = 'Item'
	visible = False 
	aliases = ['map', 'blueprint', 'plans']
	descriptions = {'desc': "They're blueprints to the mansion. There's a floorplan on one of the pages. If you take these with you, you'll be able to navigate better.",
					'takeBP': "You take the blueprints. With the floorplan, you'll be able to navigate better.",
					'alreadyTakenBP': "You already took that.",
					'touchBP': "You touch the blueprints. Nothing happens.",
					'eatBP': "Why?",
					'dropNoHold': "You have to pick up a thing to drop it.",
					'dropBP': "You put down the blueprints. Already you feel lost."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		if eng.inInventory(self):
			return self.descriptions['alreadyTakenBP']
		else:
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['takeBP']


	def touch(self):
		return self.descriptions['touchBP']


	def drop(self):
		if eng.inInventory(self) == False:
			return self.descriptions['dropNoHold']
		else:
			eng.removeFromInventory(self)
			eng.dropItem(self)
			return self.descriptions['dropBP']


	def eat(self, otherThing):
		return self.descriptions['eatBP']



blueprints = Blueprints()
eng.setupItem(blueprints)