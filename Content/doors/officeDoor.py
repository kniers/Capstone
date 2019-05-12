import eng

class officeDoor:
	name = 'officeDoor'
	visible = True 
	aliases = ['door']
	roomConnections = {'north': 'Hallway', 'south': 'Office'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It's from the hall to the office."}
	properties = {'locked': False}
	
	
	def go(self):
		office = eng.getRoomByName('Office')
		hall = eng.getRoomByName('Hallway')
		currRoom = eng.getCurrentRoom()
		if currRoom == office:
			return eng.goToRoom(hall)
		else:
			return eng.goToRoom(office)

			
	def look(self):
		return self.descriptions['desc']

		
	# get connection from the perspective of the room the player is currently in
	def getConnection(self, direction):
		if direction in self.roomConnections:
			return self.roomConnections[direction]
		else:
			return 'No room in that direction'



officeDoor = officeDoor()
eng.setupDoor(officeDoor)