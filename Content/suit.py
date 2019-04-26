class Suit:
	def __init__(self, name, aliases, description, items, properties):
		self.name = name
		self.type = "Item"
		self.aliases = aliases
		self.description = description
		self.viewed = False 
		self.items = items
		self.properties = properties 

	def setViewed(self):
		self.viewed = True
		
	def getViewed(self):
		return self.viewed 
	
	def isAlias(self, alias):
		if alias in self.aliases:
			return True
		else:
			return False 
	
	# Verb to get description of item  	
	def look(self):
		self.viewed = True #Boolean 'viewed' can be used to print different descriptions in some cases
		return self.description
	
	# Other verb. Suit isn't too complicated. Most items will have multiple of these functions.
	def wear(self):
		if 'wearing' not in self.properties:
			self.properties['wearing'] = True 
			return "The suit fits perfectly. Now you're ready for the cocktail party!\n" \
				"Remember that you're here to steal stuff, not have a good time.\n"
		else:
			return "You're already wearing the suit!\n"
		

# Testing
'''
name = "suit"
aliases = ["tux", "outfit", "clothes"]
description = "What's this? It seems like a fancy suit, laid on the bed for someone to wear to the party.\nWhat size? 42 long.\nPerfect. Just your size. You'll be out of here in no time."	
suit = Suit(name, aliases, description, [], {})
print("Suit has been viewed: " + str(suit.viewed) + "\n")
print(suit.look() + "\n")
print("Suit has been viewed: " + str(suit.viewed) + "\n")
print(suit.wear())
print(suit.wear())
print("Suit is aliased by 'tux': " + str(suit.isAlias("tux")))
print("Suit not aliased by 'notAnAlias': " + str(suit.isAlias("notAnAlias")))
print(suit.type)
'''