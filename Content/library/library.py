import eng 

class Library:
	name = 'Library'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the library again. Same bookshelf. Exits to the north, east, and west. All the same. ", 
					'longDesc': "The door leads you to what looks like a library. There is a bookshelf that runs around all the free wall space. " \
								"All sorts of books line the shelves. There are doors to the north, east, and west if the books bore you too much. "}
	doors = {'north': 'foyerLibraryDoor', 'east': 'libraryBilliardRoomDoor', 'west': 'libraryStudyDoor', 'down': 'librarySecretRoomDoor'}
	items = ['The Hobbit', 'Dracula', 'Great Expectations', 'Charles Winston', 'button', 'Nathaniel Winston', 'bookshelf']
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


library = Library()
eng.setupRoom(library) 
