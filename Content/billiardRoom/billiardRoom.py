import eng 

class BilliardRoom:
	name = 'Billiard Room'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the billiard room again. ", 
					'longDesc': "The door leads you to what looks like a billiard room, with a billards table in the middle. "}
	doors = {'north': 'galleryBilliardRoomDoor', 'east': 'billiardRoomConservatoryDoor', 'west': 'libraryBilliardRoomDoor'}
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


billiardRoom = BilliardRoom()
eng.setupRoom(billiardRoom) 