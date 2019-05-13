import eng

class FoyerBallroomDoor:
	name = 'foyerBallroomDoor'
	visible = True 
	aliases = ['door']
	roomConnections = {'north': 'Ballroom', 'south': 'Foyer'}
	descriptions = {'desc': "This is the door that leads form the foyer into the ballroom."}
	properties = {'locked': False}
	
	
	def go(self):
		ballroom = eng.getRoomByName('Ballroom')
		foyer = eng.getRoomByName('Foyer')
		currRoom = eng.getCurrentRoom()
		if currRoom == ballroom:
			return eng.goToRoom(foyer)
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


foyerBallroom = FoyerBallroomDoor()
eng.setupDoor(foyerBallroom)