import eng 

class FrontPorch:
	name = 'Front Porch'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're on the front porch. ", 
					'longDesc': "The door leads you to the porch at the front of the house. "}
	doors = {'east': 'frontDoor'} #, 'north': 'ballroom', 'east': 'portraitGallery', 'west': 'frontPorch'}
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


frontPorch = FrontPorch()
eng.setupRoom(frontPorch) 