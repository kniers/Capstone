import eng

class Staircase:
	name = 'staircase'
	visible = True 
	aliases = ['stair', 'stairs', 'stairway']
	roomConnections = {'up': 'Hallway', 'down': 'Foyer'}
	descriptions = {'desc': "It's a staircase. I'm sure you've used them before in your life. You can handle it. "}
	properties = {'locked': False}

	
	def go(self):
		foyer = eng.getRoomByName('Foyer')
		hall = eng.getRoomByName('Hallway')
		currRoom = eng.getCurrentRoom()
		if currRoom == foyer:
			return eng.goToRoom(hall)
		else:
			return eng.goToRoom(foyer)


	def look(self):
		return self.descriptions['desc']


staircase = Staircase()
eng.setupDoor(staircase)