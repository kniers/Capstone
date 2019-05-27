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
			# Can't go downstairs holding the masterpiece from the hallway
			masterpiece = eng.getItemByName('masterpiece')
			if eng.inInventory(masterpiece):
				return "Going downstairs to the party while holding this huge stolen painting isn't the best idea you've had. You should drop it."
			return eng.goToRoom(foyer)


	def look(self):
		return self.descriptions['desc']


staircase = Staircase()
eng.setupDoor(staircase)