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
					'dropDuck': "You put the duck down.",
					'useDuck': "You squeeze the duck. You feel a little better about your sad life.",
					'killDuck': "Why would you do that, you heartless wretch?",
					'talkDuck': "'Well, what do you think?' you ask the duck. It doesn't respond, keeping its wisdom to itself."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']


	def talk(self):
		return self.descriptions['talkDuck']


	def kill(self):
		return self.descriptions['killDuck']


	def hit(self):
		return self.descriptions['killDuck']


	def use(self):
		return self.descriptions['useDuck']
	
	
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
			eng.dropItem(self)
			return self.descriptions['dropDuck']


	def eat(self):
		return self.descriptions['eatDuck']
			

rubberDuck = RubberDuck()
eng.setupItem(rubberDuck)