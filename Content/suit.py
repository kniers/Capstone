import eng

class Suit:
	name = 'suit'
	
	def __init__(self, aliases, description, items, properties):
		self.type = "Item"
		self.aliases = aliases
		self.description = description
		self.visible = False
		self.items = items
		self.properties = properties 
	
	
	def isAlias(self, alias):
		if alias in self.aliases:
			return True
		else:
			return False 
	

	def look(self):
		self.visible = True
		return self.description
	

	def wear(self):
		if 'wearing' not in self.properties:
			self.properties['wearing'] = True 
			eng.addToInventory(self)
			currRoom = eng.getCurrentRoom()
			currRoom.removeItem('suit')
			return self.properties['putOnSuit']
		else:
			return self.properties['alreadyWearing']
	
	# Take off the suit, if player is wearing it 
	def remove(self):
		if 'wearing' not in self.properties or self.properties['wearing'] == False:
			return self.properties['removeNotWeariing']
		else:
			self.properties['wearing'] = False
			currRoom = eng.getCurrentRoom()
			currRoom.addItem('suit')
			eng.removeFromInventory(self)
			return self.properties['removeSuit']


aliases = ["tux", "outfit", "clothes"]
description = "Let's check out this suit. It's Italian, and likely expensive! What size? 42 long. Perfect. If you choose to wear that, you'll be out of here in no time."
properties = {'wearingDesc': "You're dressed in a suit, so you're safe to move around the party - just don't act weird.",
			  'removeSuit': "You've removed the suit",
			  'removeNotWearing': "How can you remove something that you're not even wearing?",
			  'alreadyWearing': "You're already wearing the suit!",
			  'putOnSuit': "The suit fits perfectly. Now you're ready for the cocktail party! " \
						   "Remember that you're here to steal stuff, not have a good time."}
suit = Suit(aliases, description, [], properties)
eng.setupItem(suit)