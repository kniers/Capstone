import eng

class FoyerGalleryDoor:
	name = 'foyerGalleryDoor'
	visible = True 
	aliases = ['door']
	roomConnections = {'east': 'Portrait Gallery', 'west': 'Foyer'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen."}
	properties = {'locked': False}	
			
	
	def go(self):
		foyer = eng.getRoomByName('Foyer')
		gallery = eng.getRoomByName('Portrait Gallery')
		currRoom = eng.getCurrentRoom()
		if currRoom == foyer:
			return eng.goToRoom(gallery)
		else:
			return eng.goToRoom(foyer)


	def look(self):
		return self.description


foyerGalleryDoor = FoyerGalleryDoor()
eng.setupDoor(foyerGalleryDoor)