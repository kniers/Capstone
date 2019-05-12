import eng

class masterBathDoor:
	name = 'masterBathDoor'
	visible = True 
	aliases = ['door']
	roomConnections = {'north': 'Master Bathroom', 'south': 'Master Bedroom'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen."}
	properties = {'locked': False}	
			
	
	def go(self):
		masterBed = eng.getRoomByName('Master Bedroom')
		masterBath = eng.getRoomByName('Master Bathroom')
		currRoom = eng.getCurrentRoom()
		if currRoom == masterBed:
			return eng.goToRoom(masterBath)
		else:
			return eng.goToRoom(masterBed)


	def look(self):
		return self.description

		
	# get connection from the perspective of the room the player is currently in
	def getConnection(self, direction):
		if direction in self.roomConnections:
			return self.roomConnections[direction]
		else:
			return 'No room in that direction'


masterBathDoor = masterBathDoor()
eng.setupDoor(masterBathDoor)


