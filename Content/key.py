import eng

class Key:
	name = 'key'
	
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
	
	# Other verb. Suit isn't too complicated. Most items will have multiple of these functions.
	def take(self):
		# get current inventory
		# if key in inventory	
		if eng.inInventory('key'):
			# you are already carrying the key
			return "You're already carrying the key."
		#else
		else:
			# add key to inventory
			eng.addToInventory(self)
			# remove from room item list
			currRoom = eng.getCurrentRoom()
			currRoom.removeItem('key')
			return "You've picked up the key. Who knows what door you'll need it for, but it'll probably be useful."
	
	# Drop the key 
	def drop(self):
		# if key not in inventory
		if eng.inInventory('key') == False:
			# can't drop it, you don't even have it
			return "You can't drop the key, you aren't holding it!"
		# else
		else:
			# add key to current room item list
			currRoom = eng.getCurrentRoom()
			currRoom.addItem('key')
			# remove from inventory
			eng.removeFromInventory(self)
			# return string to describe what has been done
			return "You dropped the key back into the nightstand where you found it. Don't want to place it anywhere else and raise suspicion."


aliases = []
description = "This is a pretty standard key in terms of appearance."
key = Key(aliases, description, [], {})
eng.setupItem(key)