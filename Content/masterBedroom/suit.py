import eng

class Suit:
	name = 'suit'
	#type = 'Item'
	visible = False 
	aliases = ['tux', 'outfit']
	descriptions = {'desc': "Let's check out this suit. It's Italian, and likely expensive! What size? 42 long. Perfect. If you choose to wear that, you'll be out of here in no time. Hey, there's a red and blue tie too.",
					'wearingDesc': "You're dressed in a suit, so you're safe to move around the party - just don't act weird.",
					'removeSuit': "You've removed the suit",
					'dontStrip': "If you're trying not to be noticed, you probably don't want to strip.",
					'removeNotWearing': "How can you remove something that you're not even wearing?",
					'alreadyWearing': "You're already wearing the suit!",
					'putOnSuit': "The suit fits perfectly. Now you're ready for the cocktail party! " \
								 "Remember that you're here to steal stuff, not have a good time."}
	properties = {'wearing': False}
	

	def look(self):
		self.visible = True
		return self.descriptions['desc']


	def take(self):
		return self.wear()
	

	def wear(self):
		returnMe = ""
		gown = eng.getItemByName("gown")
		if gown.properties['wearing']:
			returnMe = gown.remove() + "\n\n"
		if self.properties['wearing'] == False:
			self.properties['wearing'] = True 
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return returnMe + self.descriptions['putOnSuit']
		else:
			return returnMe + self.descriptions['alreadyWearing']
	
	# Take off the suit, if player is wearing it
	# This function is not accessible in normal gameplay
	def remove(self):
		currRoom = eng.getCurrentRoom()
		if currRoom.name != "Master Bedroom":
			return self.descriptions['dontStrip']
		if self.properties['wearing'] == False:
			return self.descriptions['removeNotWeariing']
		else:
			self.properties['wearing'] = False
			eng.removeFromInventory(self)
			eng.dropItem(self)
			return self.descriptions['removeSuit']


suit = Suit()
eng.setupItem(suit)