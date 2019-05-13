import eng

class FoyerLibraryDoor:
	name = 'foyerLibraryDoor'
	visible = True 
	aliases = ['door', 'library door']
	roomConnections = {'north': 'Foyer', 'south': 'Library'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen."}
	properties = {'locked': False}
	
	
	def go(self):
		foyer = eng.getRoomByName('Foyer')
		library = eng.getRoomByName('Library')
		currRoom = eng.getCurrentRoom()
		if currRoom == foyer:
			return eng.goToRoom(library)
		else:
			return eng.goToRoom(foyer)


	def look(self):
		return self.descriptions['desc']

		
	# get connection from the perspective of the room the player is currently in
	def getConnection(self, direction):
		if direction in self.roomConnections:
			return self.roomConnections[direction]
		else:
			return 'No room in that direction'


foyerLibraryDoor = FoyerLibraryDoor()
eng.setupDoor(foyerLibraryDoor)