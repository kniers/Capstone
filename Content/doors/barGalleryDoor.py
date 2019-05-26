import eng

class BarGalleryDoor:
	name = 'barGalleryDoor'
	visible = True 
	aliases = ['door', 'gallery door']
	roomConnections = {'north': 'Bar', 'south': 'Portrait Gallery'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen."}
	properties = {'locked': False}
	
	
	def go(self):
		bar = eng.getRoomByName('Bar')
		gallery = eng.getRoomByName('Portrait Gallery')
		currRoom = eng.getCurrentRoom()
		if currRoom == bar:
			return eng.goToRoom(gallery)
		else:
			return eng.goToRoom(bar)


	def look(self):
		return self.descriptions['desc']


barGalleryDoor = BarGalleryDoor()
eng.setupDoor(barGalleryDoor)