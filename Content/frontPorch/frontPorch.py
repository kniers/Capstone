import eng 

class FrontPorch:
	name = 'Front Porch'
	visited = False
	visible = False
	aliases = ['outside']
	descriptions = {'shortDesc': "You're on the front porch. ", 
					'longDesc': "The door leads you to the porch at the front of the house. Several luxary cars are parked by the house. At the other end of the long driveway is a guard shack. ",
					'bethal': "The old lady from the foyer is now out here calling for the guards. The jig is up. You'll never get past the guards. You need to find another way out, and quick!"}
	doors = {'east': 'frontDoor'} #, 'north': 'ballroom', 'east': 'portraitGallery', 'west': 'frontPorch'}
	items = ['cars', 'guards', 'guard shack']
	properties = {'initialized': False}

			
	def _printShortDesc(self):
		description = self.descriptions['shortDesc']
		if 'old lady' in self.items:
			description += self.descriptions['bethal']
		return description

			
	def _printLongDesc(self):
		if self.properties['initialized'] == False:
			self.properties['initialized'] = True
		
		description = self.descriptions['longDesc']
		if 'old lady' in self.items:
			description += self.descriptions['bethal']
		return description

		
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