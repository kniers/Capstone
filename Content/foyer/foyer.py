import eng 

class Foyer:
	name = 'Foyer'
	visited = False
	visible = False
	aliases = ['inside']
	descriptions = {'shortDesc': "You're in the foyer again. " \
								 "You have exits in all directions to choose from. ", 
					'longDesc': "You're in the grand foyer at the front of the house. A dazzling chandelier hangs from the ceiling. " \
								"Besides the staircase you came down earlier, there are doors in each direction. The one to the west looks like " \
								"the entrance to the house. The other three... it's difficult to tell where they lead. ",
					'drink': "A server sees you are empty handed and offers you a martini. You accept the drink just to fit in with the party.",
					'bethal': "There is an old lady sitting near the stairwell."}
	doors = {'up': 'staircase', 'west': 'frontDoor', 'north': 'foyerBallroomDoor', 'east': 'foyerGalleryDoor', 'south': 'foyerLibraryDoor'}
	items = ['chandelier', 'martini', 'drink server', 'old lady']
	properties = {'initialized': False}

			
	def _printShortDesc(self): 
		description = self.descriptions['shortDesc']
		if 'old lady' in self.items:
			description += self.descriptions['bethal']
		return description

			
	def _printLongDesc(self):
		if self.properties['initialized'] == False:
			self.properties['initialized'] = True
		
		description = self.descriptions['longDesc']
		if 'old lady' in self.items:
			description += self.descriptions['bethal']
		return description

		
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
