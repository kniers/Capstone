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


galleryBilliardRoomDoor = GalleryBilliardRoomDoor()
eng.setupDoor(galleryBilliardRoomDoor)