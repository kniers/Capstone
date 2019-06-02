import eng 

class BilliardRoom:
	name = 'Billiard Room'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the billiard room again. You've got exits to the north, east, and west. ", 
					'longDesc': "The door leads you to what looks like a billiard room, with a billiard table in the middle. " \
								"Decorative plants are lined up along the wall. " \
								"There are doors out of this room to the north, east, and west, whenever you're ready. ",
					'players': "Some low hanging lights illuminate the table where two gentlemen are finishing up a game of 8-ball. ",
					'noPlayers': "No one else is in here. Time to take a closer look around. "}
	doors = {'north': 'galleryBilliardRoomDoor', 'east': 'billiardRoomConservatoryDoor', 'west': 'libraryBilliardRoomDoor'}
	items = ['billiard table', 'billiard players', 'billiard lights', 'decorative plants', 'light switch', 'table lever', 'Ruby']
	properties = {'initialized': False, 'players': True}
			
	def _printShortDesc(self): 
		return self.descriptions['shortDesc']

			
	def _printLongDesc(self):
		if self.properties['initialized'] == False:
			self.properties['initialized'] = True
		
		description = self.descriptions['longDesc']
		if 'billiard players' in self.items:
			description += self.descriptions['players']
		else:
			description += self.descriptions['noPlayers']

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


billiardRoom = BilliardRoom()
eng.setupRoom(billiardRoom) 