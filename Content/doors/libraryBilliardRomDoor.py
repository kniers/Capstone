import eng

class LibraryBilliardRoomDoor:
	name = 'libraryBilliardRoomDoor'
	visible = True 
	aliases = ['door']
	roomConnections = {'east': 'Billiard Room', 'west': 'Library'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen."}
	properties = {'locked': False}
	
	
	def go(self):
		library = eng.getRoomByName('Library')
		billiardRoom = eng.getRoomByName('Billiard Room')
		currRoom = eng.getCurrentRoom()
		if currRoom == library:
			return eng.goToRoom(billiardRoom)
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


libraryBilliardRoomDoor = LibraryBilliardRoomDoor()
eng.setupDoor(libraryBilliardRoomDoor)