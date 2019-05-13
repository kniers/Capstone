import eng

class FrontDoor:
	name = 'frontDoor'
	visible = True 
	aliases = ['door', 'front door']
	roomConnections = {'east': 'Foyer', 'west': 'Front Porch'}
	descriptions = {'desc': "This is the door out of the house."}
	properties = {'locked': False}
	
	
	def go(self):
		foyer = eng.getRoomByName('Foyer')
		frontPorch = eng.getRoomByName('Front Porch')
		currRoom = eng.getCurrentRoom()
		if currRoom == foyer:
			return eng.goToRoom(frontPorch)
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


frontDoor = FrontDoor()
eng.setupDoor(frontDoor)