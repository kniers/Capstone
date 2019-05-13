import eng 

class PortraitGallery:
	name = 'Portrait Gallery'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the portrait gallery again. ", 
					'longDesc': "The door leads you to what looks like a... portrait gallery? "}
	doors = {'north': 'barGalleryDoor', 'west': 'foyerGalleryDoor', 'south': 'galleryBilliardRoomDoor'}
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


portraitGallery = PortraitGallery()
eng.setupRoom(portraitGallery) 