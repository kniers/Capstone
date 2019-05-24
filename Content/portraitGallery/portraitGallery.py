import eng 

class PortraitGallery:
	name = 'Portrait Gallery'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the portrait gallery again. ", 
				'longDesc': "The door leads you to an art gallery. One wall is covered in portraits of former residents of the mansion. They look down disapprovingly at you. The opposite wall contains mostly paintings of naked mythological figures in various seductive poses, but there's a landscape and a still life that look interesting. ",
				'criticFragmentA': " There's a male critic looking at one of the portraits.",
				'criticFragmentB': " There's a female critic looking at the large landscape."}
	doors = {'north': 'barGalleryDoor', 'west': 'foyerGalleryDoor', 'south': 'galleryBilliardRoomDoor'}
	items = ['still life', 'landscape', 'portraits', 'male critic', 'female critic', 'cabinet key']
	properties = {'initialized': False}

			
	def _printShortDesc(self): 
		return self.descriptions['shortDesc']

			
	def _printLongDesc(self):
		if self.properties['initialized'] == False:
			self.properties['initialized'] = True

		sayMe = self.descriptions['longDesc']
		if 'female critic' in self.items:
			sayMe = sayMe + criticFragmentB
		if 'male critic' in self.items:
			sayMe = sayMe + criticFragmentA
		
		return sayMe

		
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