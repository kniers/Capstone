import eng 

class Ballroom:
	name = 'Ballroom'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the ballroom again. ", 
					'longDesc': "The door leads you to what looks like a grand ballroom. Several couples are dancing in their own little worlds. One of the more striking features of the room is a large statue at the end."}
	doors = {'south': 'foyerBallroomDoor', 'north': 'ballroomKitchenDoor', 'east': 'ballroomBarDoor', 'west': 'ballroomBathroomDoor'}
	items = ['rodin statue']
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


ballroom = Ballroom()
eng.setupRoom(ballroom) 