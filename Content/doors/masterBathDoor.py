import eng

class masterBathDoor:
	name = 'masterBathDoor'
	visible = True 
	aliases = []
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
		return self.descriptions['desc']


masterBathDoor = masterBathDoor()
eng.setupDoor(masterBathDoor)