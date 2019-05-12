import eng

class Gown:
	name = 'gown'
	#type = 'Item'
	visible = False
	aliases = ['dress']
	descriptions = {'desc': "What's this? A beautiful gown. Great for cocktail parties!",
					'wearingDesc': "You're dressed in a gown, so you're safe to move around the party - just don't act weird.",
					'alreadyWearing': "You're already wearing the gown! ",
					'putOnGown': "The gown fits perfectly. Now you're ready for the cocktail party! Remember that you're here to steal stuff, not have a good time.",
					'remove': "You've removed the gown", 
					'removeNotWearing': "How can you remove something that you're not even wearing? "}
	properties = {'wearing': False}
		

	def look(self):
		self.visible = True
		return self.descriptions['desc']
	

	def wear(self):
		if self.properties['wearing'] == False:
			self.properties['wearing'] = True 
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['putOnGown']
		else:
			return self.descriptions['alreadyWearing']
		
		
	# Take off the gown, if player is wearing it 
	def remove(self):
		if self.properties['wearing'] == False:
			return self.descriptions['removeNotWearing']
		else:
			self.properties['wearing'] = False
			eng.removeFromInventory(self)
			currRoom = eng.getCurrentRoom()
			currRoom.addItem('gown')
			return self.descriptions['remove']
		
		
gown = Gown()
eng.setupItem(gown)