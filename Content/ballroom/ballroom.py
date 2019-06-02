import eng 

class Ballroom:
	name = 'Ballroom'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the ballroom again. It looks like the CEO of Old Money Corp is here. He looks very popular. ",
					'longDesc': "The door leads you to what looks like a grand ballroom. " \
								"One couple dances by, off in their own little world. Another couple is sitting at a table, chatting quietly. " \
								"One of the more striking features of the room is a large statue at the end. ", 
					'doorDesc': "There are doors to the east and west, swinging doors to the north where staff are entering and leaving, " \
								"and a set of double doors to the south that lead out to the foyer. "}
	doors = {'south': 'foyerBallroomDoor', 'north': 'ballroomKitchenDoor', 'east': 'ballroomBarDoor', 'west': 'ballroomBathroomDoor'}
	items = ['rodin statue', 'dancing couple', 'sitting couple', 'CharlesWinston4']
	properties = {'initialized': False}

			
	def _printShortDesc(self): 
		return self.descriptions['shortDesc'] + self.descriptions['doorDesc']

			
	def _printLongDesc(self):
		if self.properties['initialized'] == False:
			self.properties['initialized'] = True
		
		return self.descriptions['longDesc'] + self.descriptions['doorDesc']

		
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
