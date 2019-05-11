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
	
	
	def look(self):
		self.visible = True
		return self.description
	
	
	def take(self):
		if eng.inInventory(self):
			return self.properties['alreadyTakenKey']
		else:
			# add key to inventory
			eng.addToInventory(self)
			# remove from room item list
			# Now automatic with addToInventory()!
			#currRoom = eng.getCurrentRoom()
			#currRoom.removeItem('key')
			return self.properties['takeKey']
	

	def drop(self):
		if eng.inInventory(self) == False:
			return self.properties['dropNoHold']
		else:
			eng.removeFromInventory(self)
			currRoom = eng.getCurrentRoom()
			currRoom.addItem('key')
			return self.properties['drop']



aliases = []
description = "This is a pretty standard key in terms of appearance."
properties = {'dropNoHold': "You can't drop the key, you aren't holding it!", 
			  'drop': "You dropped the key back into the nightstand where you found it. Don't want to place it anywhere else and raise suspicion.", 
			  'alreadyTakenKey': "You're already carrying the key.", 
			  'takeKey': "You've picked up the key. Who knows what door you'll need it for, but it'll probably be useful."}
key = Key(aliases, description, [], properties)
eng.setupItem(key)