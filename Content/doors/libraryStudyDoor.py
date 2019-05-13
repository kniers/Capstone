import eng

class LibraryStudyDoor:
	name = 'libraryStudyDoor'
	visible = True 
	aliases = ['door', 'study door']
	roomConnections = {'east': 'Library', 'west': 'Study'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen."}
	properties = {'locked': False}
	
	
	def go(self):
		library = eng.getRoomByName('Library')
		study = eng.getRoomByName('Study')
		currRoom = eng.getCurrentRoom()
		if currRoom == library:
			return eng.goToRoom(study)
		else:
			return eng.goToRoom(library)


	def look(self):
		return self.descriptions['desc']

		
	# get connection from the perspective of the room the player is currently in
	def getConnection(self, direction):
		if direction in self.roomConnections:
			return self.roomConnections[direction]
		else:
			return 'No room in that direction'


libraryStudyDoor = LibraryStudyDoor()
eng.setupDoor(libraryStudyDoor)