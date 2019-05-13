import eng

class Staircase:
	name = 'staircase'
	visible = True 
	aliases = ['stair', 'stairs', 'stairway']
	roomConnections = {'up': 'Hallway', 'down': 'Foyer'}
	descriptions = {'desc': "It's a staircase. I'm sure you've used them before in your life. You can handle it. "}
	properties = {'locked': False}

	
	def go(self):
		foyer = eng.getRoomByName('Foyer')
		hall = eng.getRoomByName('Hallway')
		currRoom = eng.getCurrentRoom()
		if currRoom == foyer:
			return eng.goToRoom(hall)
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


staircase = Staircase()
eng.setupDoor(staircase)