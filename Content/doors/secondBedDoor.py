import eng

class SecondBedDoor:
	name = 'secondBedDoor'
	visible = True 
	aliases = ['door']
	roomConnections = {'east': 'Hallway', 'west': 'Second Bedroom'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It's from the hall to the guest bedroom."}
	properties = {'locked': False}

	
	def go(self):
		bedroom = eng.getRoomByName('Second Bedroom')
		hall = eng.getRoomByName('Hallway')
		currRoom = eng.getCurrentRoom()
		if currRoom == bedroom:
			return eng.goToRoom(hall)
		else:
			return eng.goToRoom(bedroom)


	def look(self):
		return self.descriptions['desc']

		
	# get connection from the perspective of the room the player is currently in
	def getConnection(self, direction):
		if direction in self.roomConnections:
			return self.roomConnections[direction]
		else:
			return 'No room in that direction'


secondBedDoor = SecondBedDoor()
eng.setupDoor(secondBedDoor)