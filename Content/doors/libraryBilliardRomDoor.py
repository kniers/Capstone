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


libraryBilliardRoomDoor = LibraryBilliardRoomDoor()
eng.setupDoor(libraryBilliardRoomDoor)