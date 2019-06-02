import eng

class LibrarySecretRoomDoor:
	name = 'librarySecretRoomDoor'
	visible = False 
	aliases = ['iron hatch', 'hatch']
	roomConnections = {'up': 'Library', 'down': 'Secret Room'}
	descriptions = {'desc': "It is an old iron hatch. Looks very sturdy.",
				'lockedDoor': "The hatch is locked. ",
				'unlockFail': "The lock didn't turn",
				'unlockSuccess': "The old lock creeks and turns. The hatch opens to a stone stairwell leading downward. ",
				'alreadyOpen': "It's already open. You can head down now. "}
	properties = {'locked': True}

	def open(self, otherThing):
		if self.properties['locked']:
			if otherThing is None:
				return "It's locked"
				
				# forcing player to explicitly unlock with bone key
				#key = eng.getItemByName('bone key')
				#if eng.inInventory(key):
				#	return self._unlockDoor()
				#else:
				#	return self.descriptions['unlockFail']
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
