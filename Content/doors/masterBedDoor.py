import eng

class masterBedDoor:
	name = 'masterBedDoor'
	visible = True 
	aliases = ['door', 'hallway door']
	roomConnections = {'east': 'Master Bedroom', 'west': 'Hallway'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen."}
	properties = {'locked': False}
	
	
	def go(self):
		masterBed = eng.getRoomByName('Master Bedroom')
		hall = eng.getRoomByName('Hallway')
		currRoom = eng.getCurrentRoom()
		if currRoom == masterBed:
			return eng.goToRoom(hall)
		else:
			return eng.goToRoom(masterBed)


	def look(self):
		return self.descriptions['desc']

		
	# get connection from the perspective of the room the player is currently in
	def getConnection(self, direction):
		if direction in self.roomConnections:
			return self.roomConnections[direction]
		else:
			return 'No room in that direction'


masterBedDoor = masterBedDoor()
eng.setupDoor(masterBedDoor)