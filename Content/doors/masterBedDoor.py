import eng

class masterBedDoor:
	name = 'masterBedDoor'
	visible = True 
	aliases = ['door', 'hallway door']
	roomConnections = {'east': 'Master Bedroom', 'west': 'Hallway'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen.",
			'underdressed': "Hold on! You can't mingle looking like that. You'd stand out like a watermelon in a bowl full of chick peas.",
			'unlockNone': "The door is locked. You can't force it, somebody might hear you.",
			'unlockFail': "That won't work.",
			'unlockSuccess': "The key fits. You open the door with ease."}
	properties = {'locked': True}
	
	
	def go(self):
		if self.properties['locked']:
			return self.descriptions['unlockNone']
		else:
			suit = getItemByName('suit')
			gown = getItemByname('gown')
			if suit.properties['wearing'] or gown.properties['wearing']:
				masterBed = eng.getRoomByName('Master Bedroom')
				hall = eng.getRoomByName('Hallway')
				currRoom = eng.getCurrentRoom()
				if currRoom == masterBed:
					return eng.goToRoom(hall)
				else:
					return eng.goToRoom(masterBed)
			else:
				return self.descriptions['underdressed']


	def look(self):
		return self.descriptions['desc']


	def open(self, otherThing):
		if otherThing is None:
			return self.descriptions['unlockNone']
		elif otherThing is bedroomKey:
			self.properties['locked'] = False
			return self.descriptions['unlockSuccess']
		else:
			return self.descriptions['unlockFail']

		
masterBedDoor = masterBedDoor()
eng.setupDoor(masterBedDoor)
