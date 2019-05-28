import eng

class masterBedDoor:
	name = 'masterBedDoor'
	visible = True 
	aliases = ['door', 'hallway door']
	roomConnections = {'east': 'Master Bedroom', 'west': 'Hallway'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen.",
			'lockedDoor': "It's locked. Hopefully there's a spare key in here somewhere.",
			'alreadyOpen': "You already opened the door.",
			'unlockSuccess': "The key fits. You unlock the door and leave it open.",
			'unlockFail': "That won't work.",
			'notDressed': "Hold up now! You're not dressed for the party! You'll stand out like a watermelon in a bowl full of chick peas!"}
	properties = {'locked': True}
	
	
	def go(self):
		if self.properties['locked']:
			return self.descriptions['lockedDoor']
		suit = eng.getItemByName("suit")
		gown = eng.getItemByName("gown")
		if suit.properties['wearing'] or gown.properties['wearing']:
			masterBed = eng.getRoomByName('Master Bedroom')
			hall = eng.getRoomByName('Hallway')
			currRoom = eng.getCurrentRoom()
			if currRoom == masterBed:
				return eng.goToRoom(hall)
			else:
				return eng.goToRoom(masterBed)
		else:
			return self.descriptions['notDressed']


	def look(self):
		return self.descriptions['desc']


	def open(self, otherThing):
		if self.properties['locked']:
			if otherThing.name == 'bedroom key':
				self.properties['locked'] = False
				return self.descriptions['unlockSuccess']
			else:
				return self.descriptions['unlockFail']
		else:
			return self.descriptions['alreadyOpen']

		
	# get connection from the perspective of the room the player is currently in
	def getConnection(self, direction):
		if direction in self.roomConnections:
			return self.roomConnections[direction]
		else:
			return 'No room in that direction'


masterBedDoor = masterBedDoor()
eng.setupDoor(masterBedDoor)