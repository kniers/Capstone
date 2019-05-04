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
	
	# Verb to get description of item  	
	def look(self):
		self.visible = True #Boolean 'visible' can be used to print different descriptions in some cases
		return self.description
	
	# Other verb. Gown isn't too complicated. Most items will have multiple of these functions.
	def wear(self):
		if 'wearing' not in self.properties:
			self.properties['wearing'] = True 
			eng.addToInventory(self)
			currRoom = eng.getCurrentRoom()
			currRoom.removeItem('gown')
			return "The gown fits perfectly. Now you're ready for the cocktail party!\n" \
				"Remember that you're here to steal stuff, not have a good time.\n"
		else:
			return "You're already wearing the gown!\n"
			
	# Take off the gown, if player is wearing it 
	def remove(self):
		if 'wearing' not in self.properties or self.properties['wearing'] == False:
			return "How can you remove something that you're not even wearing?"
		else:
			self.properties['wearing'] = False
			currRoom = eng.getCurrentRoom()
			currRoom.addItem('gown')
			eng.removeFromInventory(self)
			return "You've removed the gown"
		


aliases = ["dress"]
description = "What's this? A beautiful gown. Great for cocktail parties!"
gown = Gown(aliases, description, [], {})
eng.setupItem(gown)