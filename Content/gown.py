import eng

class Gown:
	name = 'gown'
	
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
			currRoom.removeItem('gown')
			return self.properties['putOnGown']
		else:
			return self.properties['alreadyWearing']
		
		
	# Take off the gown, if player is wearing it 
	def remove(self):
		if 'wearing' not in self.properties or self.properties['wearing'] == False:
			return self.properties['removeNotWearing']
		else:
			self.properties['wearing'] = False
			currRoom = eng.getCurrentRoom()
			currRoom.addItem('gown')
			eng.removeFromInventory(self)
			return self.properties['remove']
		


aliases = ["dress"]
description = "What's this? A beautiful gown. Great for cocktail parties!"
properties = {'wearingDesc': "You're dressed in a gown, so you're safe to move around the party - just don't act weird.",
			  'alreadyWearing': "You're already wearing the gown! ",
			  'putOnGown': "The gown fits perfectly. Now you're ready for the cocktail party! Remember that you're here to steal stuff, not have a good time.",
			  'remove': "You've removed the gown", 
			  'removeNotWearing': "How can you remove something that you're not even wearing? "}
gown = Gown(aliases, description, [], properties)
eng.setupItem(gown)