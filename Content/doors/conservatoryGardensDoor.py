import eng

class ConservatoryGardensDoor:
	name = 'conservatoryGardensDoor'
	visible = True 
	aliases = ['door']
	roomConnections = {'north': 'Gardens', 'south': 'Conservatory'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen."}
	properties = {'locked': False}
	
	
	def go(self):
		conservatory = eng.getRoomByName('Conservatory')
		gardens = eng.getRoomByName('Gardens')
		currRoom = eng.getCurrentRoom()
		if currRoom == conservatory:
			return eng.goToRoom(gardens)
		else:
			return eng.goToRoom(conservatory)


	def look(self):
		return self.descriptions['desc']

		
	# get connection from the perspective of the room the player is currently in
	def getConnection(self, direction):
		if direction in self.roomConnections:
			return self.roomConnections[direction]
		else:
			return 'No room in that direction'


conservatoryGardensDoor = ConservatoryGardensDoor()
eng.setupDoor(conservatoryGardensDoor)