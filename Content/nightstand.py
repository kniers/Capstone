import eng

class Nightstand:
	name = 'nightstand'
	
	def __init__(self, aliases, description, items, properties):
		self.type = "Item"
		self.aliases = aliases
		self.description = description
		self.visible = True 
		self.items = items
		self.properties = properties 
	
	def isAlias(self, alias):
		if alias in self.aliases:
			return True
		else:
			return False 
	
	# Verb to get description of item  	
	def look(self):
		if self.properties['opened'] == True:
			currRoom = eng.getCurrentRoom()
			if 'key' in currRoom.items: # means key has not been picked up/moved, so it's in the drawer 
				return self.properties['keyDesc']
			else:
				return self.properties['noKeyDesc']
		else:
			return self.properties['closedDesc']
	
	# Other verb. Suit isn't too complicated. Most items will have multiple of these functions.
	def open(self):
		if self.properties['opened'] == True:
			# already opened. print some snarky message
			return self.properties['alreadyOpenDesc']
		else:
			self.properties['opened'] = True
			# get current room
			currRoom = eng.getCurrentRoom() 
			# set key to visible and add to items list of current room 
			key = eng.getItemByName('key')
			if key is not None:
				key.visible = True
				currRoom.addItem('key')				
			return self.look()
		


aliases = ["dresser"]
description = "It's a nightstand with one drawer."
			  
items = ['key']
properties = {'opened': False, 
			'closedDesc': "There's nothing interesting on top of the nightstand but there may be something in the drawer.",
			'keyDesc': "The drawer is empty except for a key hidden in the back corner of the drawer.",
			'noKeyDesc': "There's nothing in the drawer. BORING.",
			'alreadyOpenDesc': "You've already opened that drawer."}
nightstand = Nightstand(aliases, description, items, properties)
eng.setupItem(nightstand)