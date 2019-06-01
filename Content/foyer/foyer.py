import eng 

class Foyer:
	name = 'Foyer'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the foyer again. There is an old lady sitting near the stairwell.", 
					'longDesc': "You're in the grand foyer at the front of the house. A dazzling chandelier hangs from the ceiling.",
					'drink': "A server sees you are empty handed and offers you a martini. You accept the drink just to fit in with the party."}
	doors = {'up': 'staircase', 'west': 'frontDoor', 'north': 'foyerBallroomDoor', 'east': 'foyerGalleryDoor', 'south': 'foyerLibraryDoor'}
	items = ['chandelier', 'martini', 'drink server', 'old lady']
	properties = {'initialized': False}

			
	def _printShortDesc(self): 
		return self.descriptions['shortDesc']

			
	def _printLongDesc(self):
		if self.properties['initialized'] == False:
			self.properties['initialized'] = True
		
		return self.descriptions['longDesc']

		
	def enterRoom(self):
		description = ""
		if (self.visited == True):
			description = self._printShortDesc()
		else:
			self.visited = True
			description = self._printLongDesc()
			martini = eng.getItemByName('martini')
			description += "\n\n" + self.descriptions['drink']
			eng.addToInventory(martini)
		return description
			
	# Per game requirements, look should reprint long description 
	def look(self):
		return self._printLongDesc()


foyer = Foyer()
eng.setupRoom(foyer) 
