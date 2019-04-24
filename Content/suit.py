from Item import *

class Suit(Item):
	def __init__(self,  name, aliases, description, items, properties):
		#self.wearing = False 
		Item.__init__(self, name, aliases, description, items, properties)
	
	# Verb to get description of item  	
	def look(self):
		self.setViewed() #Boolean 'viewed' can be used to print different descriptions in some cases
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

description = "What's this? It seems like a nice suit.\nWhat size? 42 long.\nPerfect. Just your size. You'll be out of here in no time."	
suit = Suit("suit", [], description, [], {})
print("Suit has been viewed: " + str(suit.hasBeenViewed()) + "\n")
print(suit.look() + "\n")
print("Suit has been viewed: " + str(suit.hasBeenViewed()) + "\n")
print(suit.wear())
print(suit.wear())
