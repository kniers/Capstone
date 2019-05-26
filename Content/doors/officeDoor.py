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


officeDoor = officeDoor()
eng.setupDoor(officeDoor)