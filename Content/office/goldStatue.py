import eng

class GoldStatue:
	name = 'gold statue'
	#type = 'Item'
	visible = False 
	aliases = ['statue']
	descriptions = {'desc': "It's a genuine, solid gold statue.",
					'takeGS': "You take the statue. What a prize!",
					'alreadyTakenGS': "You already took that.",
					'touchGS': "You touch the statue. It's solid gold.",
					'eatGS': "Gold is soft, but not that soft.",
					'dropNoHold': "That makes no sense.",
					'drop': "You reluctantly leave the statue."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		if eng.inInventory(self):
			return self.descriptions['alreadyTakenGS']
		else:
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['takeGS']


	def touch(self):
		return self.descriptions['touchGS']


	def drop(self):
		if eng.inInventory(self) == False:
			return self.descriptions['dropNoHold']
		else:
			eng.removeFromInventory(self)
			eng.dropItem(self)
			return self.descriptions['drop']


	def eat(self):
		return self.descriptions['eatGS']


goldStatue = GoldStatue()
eng.setupItem(goldStatue)
