import eng

class BallroomBarDoor:
	name = 'ballroomBarDoor'
	visible = True 
	aliases = ['door', 'bar door']
	roomConnections = {'east': 'Bar', 'west': 'Ballroom'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen."}
	properties = {'locked': False}
	
	
	def go(self):
		ballroom = eng.getRoomByName('Ballroom')
		bar = eng.getRoomByName('Bar')
		currRoom = eng.getCurrentRoom()
		if currRoom == ballroom:
			return eng.goToRoom(bar)
		else:
			return eng.goToRoom(ballroom)


	def look(self):
		return self.descriptions['desc']


ballroomBarDoor = BallroomBarDoor()
eng.setupDoor(ballroomBarDoor)