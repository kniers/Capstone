import eng

class Staircase:
	name = 'staircase'
	visible = True 
	aliases = ['stair', 'stairs', 'stairway', 'downstairs', 'upstairs']
	roomConnections = {'up': 'Hallway', 'down': 'Foyer'}
	descriptions = {'desc': "It's a staircase. I'm sure you've used them before in your life. You can handle it. ",
			'butlerDead': "You need to hide the butler's body before you go downstairs. If somebody sees it, they'll call the police, which you don't need right now.",
			'butlerAlive': "The butler is blocking the staircase. You can't sneak past without him seeing you.",
			'butlerHeld': "Really? You want to go downstairs in front of all those people down there holding the dead body of a man you killed? You need to hide the body first."}
	properties = {'locked': False}

	
	def go(self):
		foyer = eng.getRoomByName('Foyer')
		hall = eng.getRoomByName('Hallway')
		bt = eng.getItemByName("butler")
		if "butler" in hall.items:
			if bt.properties['dead']:
				return self.descriptions['butlerDead']
			else:
				return self.descriptions['butlerAlive']
		elif eng.inInventory(bt):
			return self.descriptions['butlerHeld']
		else:
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