class Item:
	def __init__(self, name, aliases, description, items, properties):
		self.name = name
		self.aliases = aliases
		self.description = description
		self.viewed = False 
		self.items = items
		self.properties = properties 
	
	def setViewed(self):
		self.viewed = True
	
	def hasBeenViewed(self): # Can be used to check if room description should be changed
		return self.viewed 