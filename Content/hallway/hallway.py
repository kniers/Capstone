import eng 

class Hallway:
	name = 'Hallway'
	visited = False
	visible = False 
	aliases = ['hall']
	descriptions = {'shortDesc': "You're in the hallway again. There's still nobody else around. ", 
					'longDesc': "You find yourself in the hallway. To the north is a stairwell going down. " \
								"To the south towards the end of the hallway is a door. " \
								"Across from you (west) is another door, and obviously the door you came through is behind you. "}
	doors = {'east': 'masterBedDoor', 'south': 'officeDoor', 'west': 'guestBedDoor'}
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


hallway = Hallway()
eng.setupRoom(hallway) 