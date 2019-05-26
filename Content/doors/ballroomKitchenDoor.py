import eng

class BallroomKitchenDoor:
	name = 'ballroomKitchenDoor'
	visible = True 
	aliases = ['door', 'kitchen door']
	roomConnections = {'south': 'Ballroom', 'north': 'Kitchen'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen."}
	properties = {'locked': False}
	
	
	def go(self):
		kitchen = eng.getRoomByName('Kitchen')
		ballroom = eng.getRoomByName('Ballroom')
		currRoom = eng.getCurrentRoom()
		if currRoom == kitchen:
			return eng.goToRoom(ballroom)
		else:
			return eng.goToRoom(kitchen)


	def look(self):
		return self.descriptions['desc']


ballroomKitchenDoor = BallroomKitchenDoor()
eng.setupDoor(ballroomKitchenDoor)