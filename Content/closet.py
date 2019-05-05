import eng

class Closet:
	name = 'closet'
	
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
	

	def look(self):
		if self.properties['opened'] == True:
			if 'suit' in self.items and 'gown' in self.items:
				return self.properties['openDesc'] + self.properties['bothDesc']
			elif 'suit' in self.items:
				return self.properties['openDesc'] + self.properties['suitDesc']
			elif 'gown' in self.items:
				return self.properties['openDesc'] + self.properties['gownDesc']
			else:
				return self.properties['openDesc'] + self.properties['neitherDesc']
		else:
			return self.properties['closedDesc']
	

	def open(self):
		if self.properties['opened'] == True:
			return self.properties['alreadyOpenDesc']
		else:
			self.properties['opened'] = True
			currRoom = eng.getCurrentRoom()
			suit = eng.getItemByName('suit')
			if suit is not None:
				suit.visible = True
				currRoom.addItem('suit')
			gown = eng.getItemByName('gown')
			if gown is not None:
				gown.visible = True
				currRoom.addItem('gown')				
			return self.look()
		


aliases = ["wardrobe"]
description = "It's a closet... Not much more to say about it. Open it if you'd like."
items = ['suit', 'gown']
properties = {'opened': False, 
			'closedDesc': "It's a closet... Not much more to say about it. Open it if you'd like. ",
			'openDesc': "Pretty standard closet. ",
			'suitDesc': "Theres a suit hanging in there. ",
			'gownDesc': "There's a gown hanging in there. That's about it. ",
			'bothDesc': "There's a snazzy suit in there, or a gown if that's more your style. ",
			'neitherDesc': "There's nothing in the closet. BORING. ",
			'alreadyOpenDesc': "The closet is already open. You're really trying to open it twice? What does that even mean? "}
closet = Closet(aliases, description, items, properties)
eng.setupItem(closet)