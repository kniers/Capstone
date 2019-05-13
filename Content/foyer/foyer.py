import eng 

class Foyer:
	name = 'Foyer'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the foyer again. ", 
					'longDesc': "The door leads you to the foyer at the front of the house. "}
	doors = {'up': 'staircase', 'west': 'frontDoor', 'north': 'foyerBallroomDoor', 'east': 'foyerGalleryDoor', 'south': 'foyerLibraryDoor'}
	items = []
	properties = {'initialized': False}

			
	def _printShortDesc(self): 
		return self.descriptions['shortDesc']

			
	def _printLongDesc(self):
		if self.properties['initialized'] == False:
			self.properties['initialized'] = True
		
		return self.descriptions['longDesc']

		
	def enterRoom(self):
		if (self.visited == True):
			return self._printShortDesc()
		else:
			self.visited = True
			return self._printLongDesc()

			
	# Per game requirements, look should reprint long description 
	def look(self):
		return self._printLongDesc()


foyer = Foyer()
eng.setupRoom(foyer) 