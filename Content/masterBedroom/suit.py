import eng

class Suit:
	name = 'suit'
	#type = 'Item'
	visible = False 
	aliases = ['tux', 'outfit', 'clothes']
	descriptions = {'desc': "Let's check out this suit. It's Italian, and likely expensive! What size? 42 long. Perfect. If you choose to wear that, you'll be out of here in no time.",
					'wearingDesc': "You're dressed in a suit, so you're safe to move around the party - just don't act weird.",
					'removeSuit': "You've removed the suit",
					'removeNotWearing': "How can you remove something that you're not even wearing?",
					'alreadyWearing': "You're already wearing the suit!",
					'putOnSuit': "The suit fits perfectly. Now you're ready for the cocktail party! " \
								 "Remember that you're here to steal stuff, not have a good time."}
	properties = {'wearing': False}
	

	def look(self):
		self.visible = True
		return self.descriptions['desc']
	

	def wear(self):
		if self.properties['wearing'] == False:
			self.properties['wearing'] = True 
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['putOnSuit']
		else:
			return self.descriptions['alreadyWearing']
	
	# Take off the suit, if player is wearing it 
	def remove(self):
		if self.properties['wearing'] == False:
			return self.descriptions['removeNotWeariing']
		else:
			self.properties['wearing'] = False
			eng.removeFromInventory(self)
			currRoom = eng.getCurrentRoom()
			currRoom.addItem('suit')
			return self.descriptions['removeSuit']


suit = Suit()
eng.setupItem(suit)