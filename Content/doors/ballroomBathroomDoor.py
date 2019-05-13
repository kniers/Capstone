import eng

class BallroomBathroomDoor:
	name = 'ballroomBathroomDoor'
	visible = True 
	aliases = ['door', 'bathroom door']
	roomConnections = {'east': 'Ballroom', 'west': 'Bathroom'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen."}
	properties = {'locked': False}
	
	
	def go(self):
		ballroom = eng.getRoomByName('Ballroom')
		bathroom = eng.getRoomByName('Bathroom')
		currRoom = eng.getCurrentRoom()
		if currRoom == ballroom:
			return eng.goToRoom(bathroom)
		else:
			return eng.goToRoom(ballroom)


	def look(self):
		return self.descriptions['desc']

		
	# get connection from the perspective of the room the player is currently in
	def getConnection(self, direction):
		if direction in self.roomConnections:
			return self.roomConnections[direction]
		else:
			return 'No room in that direction'


ballroomBathroomDoor = BallroomBathroomDoor()
eng.setupDoor(ballroomBathroomDoor)