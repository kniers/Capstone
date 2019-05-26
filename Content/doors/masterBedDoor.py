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

		

masterBedDoor = masterBedDoor()
eng.setupDoor(masterBedDoor)
