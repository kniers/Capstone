import eng

class RubberDuck:
	name = 'rubber duck'
	#type = 'Item'
	visible = False 
	aliases = ['rubber ducky', 'duck']
	descriptions = {'desc': "It's a perfectly average rubber duck. It looks quite intelligent for an inanimate object.",
					'takeDuck': "You pick up the duck.",
					'alreadyTakenDuck': "You already took that.",
					'touchDuck': "You touch the duck. It squeaks.",
					'eatDuck': "You raise the duck to your mouth, then you see the following warning:\n\nChoking Hazard: Not for children under three years old.",
					'dropDuck': "You put the duck down."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		if eng.inInventory(self):
			return self.descriptions['alreadyTakenDuck']
		else:
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['takeDuck']


	def touch(self):
		return self.descriptions['touchDuck']


	def drop(self):
		if eng.inInventory(self) == False:
			return self.descriptions['dropNoHold']
		else:
			eng.removeFromInventory(self)
			currRoom = eng.getCurrentRoom()
			currRoom.addItem('rubber duck')
			return self.descriptions['dropDuck']


	def eat(self, otherThing):
		return self.descriptions['eatDuck']
			

rubberDuck = RubberDuck()
eng.setupItem(rubberDuck)