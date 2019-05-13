import eng 

class Bathroom:
	name = 'Bathroom'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the bathroom off of the ballroom again. ", 
					'longDesc': "The door leads you to a small bathroom. "}
	doors = {'east': 'ballroomBathroomDoor'}
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


bathroom = Bathroom()
eng.setupRoom(bathroom) 