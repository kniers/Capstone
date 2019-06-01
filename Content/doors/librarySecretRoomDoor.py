import eng

class LibrarySecretRoomDoor:
	name = 'librarySecretRoomDoor'
	visible = False 
	aliases = ['door']
	roomConnections = {'up': 'Library', 'down': 'Secret Room'}
	descriptions = {'desc': "It is an old iron door. Looks very sturdy.",
				'lockedDoor': "The door is locked. ",
				'unlockFail': "Lock didn't turn",
				'unlockSuccess': "The old lock creeks and turns. The door opens to a stone stairwell leading downward. "}
	properties = {'locked': True}

	def open(self, otherThing):
		if self.properties['locked']:
			if otherThing is None:
				key = eng.getItemByName('bone key')
				if eng.inInventory(key):
					return self._unlockDoor()
				else:
					return self.descriptions['unlockFail']
			if otherThing.name == 'bone key':
				return self._unlockDoor()
			else:
				return self.descriptions['unlockFail']
		else:
			return self.descriptions['alreadyOpen']	
	
	def go(self):
		if self.properties['locked']:
			return self.descriptions['lockedDoor']
		library = eng.getRoomByName('Library')
		secretRoom = eng.getRoomByName('Secret Room')
		currRoom = eng.getCurrentRoom()
		if currRoom == library:
			return eng.goToRoom(secretRoom)
		else:
			return eng.goToRoom(library)


	def look(self):
		return self.descriptions['desc']

	def _unlockDoor(self):
		self.properties['locked'] = False
		secretRoom = eng.getRoomByName('Secret Room')
		secretRoom.visible = True
		return self.descriptions['unlockSuccess']

librarySecretRoomDoor = LibrarySecretRoomDoor()
eng.setupDoor(librarySecretRoomDoor)
