import eng

class GalleryBilliardRoomDoor:
	name = 'galleryBilliardRoomDoor'
	visible = True 
	aliases = ['door']
	roomConnections = {'north': 'Portrait Gallery', 'south': 'Billiard Room'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen."}
	properties = {'locked': False}
	
	
	def go(self):
		gallery = eng.getRoomByName('Portrait Gallery')
		billiardRoom = eng.getRoomByName('Billiard Room')
		currRoom = eng.getCurrentRoom()
		if currRoom == gallery:
			return eng.goToRoom(billiardRoom)
		else:
			return eng.goToRoom(gallery)


	def look(self):
		return self.descriptions['desc']

		
	# get connection from the perspective of the room the player is currently in
	def getConnection(self, direction):
		if direction in self.roomConnections:
			return self.roomConnections[direction]
		else:
			return 'No room in that direction'


galleryBilliardRoomDoor = GalleryBilliardRoomDoor()
eng.setupDoor(galleryBilliardRoomDoor)