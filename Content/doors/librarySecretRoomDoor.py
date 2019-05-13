import eng

class LibrarySecretRoomDoor:
	name = 'librarySecretRoomDoor'
	visible = True 
	aliases = ['door']
	roomConnections = {'up': 'Library', 'down': 'Secret Room'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen."}
	properties = {'locked': False}
	
	
	def go(self):
		library = eng.getRoomByName('Library')
		secretRoom = eng.getRoomByName('Secret Room')
		currRoom = eng.getCurrentRoom()
		if currRoom == library:
			return eng.goToRoom(secretRoom)
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


librarySecretRoomDoor = LibrarySecretRoomDoor()
eng.setupDoor(librarySecretRoomDoor)