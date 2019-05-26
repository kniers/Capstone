import eng

class BilliardRoomConservatoryDoor:
	name = 'billiardRoomConservatoryDoor'
	visible = True 
	aliases = ['door']
	roomConnections = {'east': 'Conservatory', 'west': 'Billiard Room'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen."}
	properties = {'locked': False}
	
	
	def go(self):
		billiardRoom = eng.getRoomByName('Billiard Room')
		conservatory = eng.getRoomByName('Conservatory')
		currRoom = eng.getCurrentRoom()
		if currRoom == billiardRoom:
			return eng.goToRoom(conservatory)
		else:
			return eng.goToRoom(billiardRoom)


	def look(self):
		return self.descriptions['desc']


billiardRoomConservatoryDoor = BilliardRoomConservatoryDoor()
eng.setupDoor(billiardRoomConservatoryDoor)