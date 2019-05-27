import eng 

class Hallway:
	name = 'Hallway'
	visited = False
	visible = False 
	aliases = ['hall']
	#FIXME: change description based on state of butler
	descriptions = {'shortDesc': "You're in the hallway again. ", 
					'longDesc': "You find yourself in the hallway. To the north is a stairwell going down. Standing at the top of the stairwell is the butler." \
								"To the south towards the end of the hallway is a door. " \
								"Across from you (west) is another door, and obviously the door you came through is behind you. ",
					'painting': "There's a magnificant painting hanging on the west wall."}
	doors = {'east': 'masterBedDoor', 'south': 'officeDoor', 'north': 'guestBedDoor', 'west': 'secondBedDoor', 'down': 'staircase'}
	items = ['butler', 'masterpiece']
	properties = {'initialized': False}

			
	def _printShortDesc(self): 
		return self.descriptions['shortDesc']

	
	def _printLongDesc(self):
		if self.properties['initialized'] == False:
			self.properties['initialized'] = True
		
		description = self.descriptions['longDesc']
		if 'masterpiece' in self.items:
			description += '\n' + self.descriptions['painting']
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


hallway = Hallway()
eng.setupRoom(hallway) 