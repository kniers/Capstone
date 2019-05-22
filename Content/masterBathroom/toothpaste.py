import eng

class Toothpaste:
	name = 'toothpaste'
	#type = 'Item'
	visible = False 
	aliases = ['tube']
	descriptions = {'desc': "It's a tube of toothpaste. Most of the paste is used, but there's still a little in there.",
					'takePaste': "You take the tube of toothpaste. Now you're equipped in the neverending war against plaque.",
					'alreadyTakenPaste': "You already took that.",
					'touchPaste': "You touch the tube. It's mostly empty inside, kind of like your soul.",
					'eatPaste': "Toothpaste contains fluoride, which can cause an upset stomach.",
					'dropNoHold': "You pick up the toothpaste and then put it back where you found it.",
					'dropPaste': "You put the toothpaste down. No dentist will tell you what to do."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		if eng.inInventory(self):
			return self.descriptions['alreadyTakenPaste']
		else:
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['takePaste']


	def touch(self):
		return self.descriptions['touchPaste']


	def drop(self):
		if eng.inInventory(self) == False:
			return self.descriptions['dropNoHold']
		else:
			eng.removeFromInventory(self)
			eng.dropItem(self)
			return self.descriptions['dropPaste']


	def eat(self):
		return self.descriptions['eatPaste']
			

toothpaste = Toothpaste()
eng.setupItem(toothpaste)