import eng

class Gown:
	name = 'gown'
	
	def __init__(self, aliases, description, items, properties):
		self.type = "Item"
		self.aliases = aliases
		self.description = description
		self.visible = True 
		self.items = items
		self.properties = properties 

	def setViewed(self):
		self.visible = True
		
	def getViewed(self):
		return self.visible 
	
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
	def equip(self):
		if 'wearing' not in self.properties:
			self.properties['wearing'] = True 
			return "The gown fits perfectly. Now you're ready for the cocktail party!\n" \
				"Remember that you're here to steal stuff, not have a good time.\n"
		else:
			return "You're already wearing the gown!\n"
		


aliases = ["dress"]
description = "What's this? A beautiful gown. Great for cocktail parties!"
suit = Suit(aliases, description, [], {})
eng.setupItem(suit)