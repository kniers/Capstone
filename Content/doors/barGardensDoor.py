import eng

class BarGardensDoor:
	name = 'barGardensDoor'
	visible = True 
	aliases = ['door', 'gardens door']
	roomConnections = {'east': 'Gardens', 'west': 'Bar'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen."}
	properties = {'locked': False}
	
	
	def go(self):
		bar = eng.getRoomByName('Bar')
		gardens = eng.getRoomByName('Gardens')
		currRoom = eng.getCurrentRoom()
		if currRoom == bar:
			return eng.goToRoom(gardens)
		else:
			return eng.goToRoom(bar)


	def look(self):
		return self.descriptions['desc']


barGardensDoor = BarGardensDoor()
eng.setupDoor(barGardensDoor)