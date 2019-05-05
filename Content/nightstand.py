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

			
	def open(self):
		if self.properties['opened'] == True:
			return self.properties['alreadyOpenDesc']
		else:
			self.properties['opened'] = True
			currRoom = eng.getCurrentRoom()
			key = eng.getItemByName('key')
			key.visible = True
			currRoom.addItem('key')				
			return self.look()
		


aliases = ["dresser", "drawer"]
description = "It's a nightstand with one drawer."	  
items = ['key']
properties = {'opened': False, 
			'closedDesc': "There's nothing interesting on top of the nightstand but there may be something in the drawer.",
			'keyDesc': "The drawer is empty except for a key hidden in the back corner of the drawer.",
			'noKeyDesc': "There's nothing in the drawer. BORING.",
			'alreadyOpenDesc': "You've already opened that drawer."}

nightstand = Nightstand(aliases, description, items, properties)
eng.setupItem(nightstand)