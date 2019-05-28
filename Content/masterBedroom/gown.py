import eng

class Gown:
	name = 'gown'
	#type = 'Item'
	visible = False
	aliases = ['dress']
	descriptions = {'desc': "What's this? A beautiful red gown with a yellow sash. Great for cocktail parties!",
					'wearingDesc': "You're dressed in a gown, so you're safe to move around the party - just don't act weird.",
					'alreadyWearing': "You're already wearing the gown! ",
					'putOnGown': "The gown fits perfectly. Now you're ready for the cocktail party! Remember that you're here to steal stuff, not have a good time.",
					'remove': "You've removed the gown",
					'dontStrip': "If you're trying not to be noticed, you probably don't want to strip.",
					'removeNotWearing': "How can you remove something that you're not even wearing? ",
					'eat': "You put the hem of the gown in your mouth. It doesn't taste very good, and it's hard to chew, so you take it out. "}
	properties = {'wearing': False}
		

	def look(self):
		self.visible = True
		return self.descriptions['desc']


	def take(self):
		self.wear()


	def eat(self):
		return self.descriptions['eatGown']
	

	def wear(self):
		suit = eng.getItemByName('suit')
		if suit.properties['wearing']:
			suit.remove()
		if self.properties['wearing'] == False:
			self.properties['wearing'] = True 
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['putOnGown']
		else:
			return self.descriptions['alreadyWearing']
		
		
	# Take off the gown, if player is wearing it 
	def remove(self):
		currRoom = eng.getCurrentRoom()
		if currRoom.name != "Master Bedroom":
			return self.descriptions['dontStrip']
		if self.properties['wearing'] == False:
			return self.descriptions['removeNotWearing']
		else:
			self.properties['wearing'] = False
			eng.removeFromInventory(self)
			eng.dropItem(self)
			return self.descriptions['remove']
		
		
gown = Gown()
eng.setupItem(gown)