import eng 

class MasterBedroom:
	name = "Master Bedroom"
	
	def __init__(self, aliases, properties, doorsToAdd, itemsToAdd):
		self.visited = False 
		self.visible = True 
		self.aliases = aliases 
		self.properties = properties
		self.doors = {}
		self.doors.update(doorsToAdd)
		self.items = []
		for itemToAdd in itemsToAdd:
			self.items.append(itemToAdd)

			
	def isAlias(self, alias):
		if alias in self.aliases:
			return True
		else:
			return False 

			
	def _printShortDesc(self): 
		return self.properties['shortDesc']

		
	# Dynamic based on what player is wearing 	
	def _printLongDesc(self):
		if self.properties['initialized'] == False:
			self.properties['initialized'] = True
			desc = self.properties['longDesc']
			desc += self.properties['noClothingDescAppend']
			return desc

		desc = self.properties['longDesc']
		suit = eng.getItemByName('suit')
		gown = eng.getItemByName('gown')
		
		if eng.inInventory(suit):
			desc += suit.properties['wearingDesc']
		elif eng.inInventory(gown):
			desc += gown.properties['wearingDesc']
		else:
			desc += self.properties['noClothingDescAppend']
		
		return desc

		
	def enterRoom(self):
		if (self.visited == True):
			return self._printShortDesc()
		else:
			self.visited = True
			return self._printLongDesc()

			
	# Per game requirements, look should reprint long description 
	def look(self):
		return self._printLongDesc()

		
	def addItem(self, item):
		self.items.append(item)
		return True

		
	def removeItem(self, itemToRemove):
		try:
			self.items.remove(itemToRemove)
			return True 
		except ValueError: #throws ValueError if item doesn't exist in list
			return False 



aliases = ["Master Bedroom", "master bed", "bedroom", "starting bedroom"]

properties = {'shortDesc': "You're back in the bedroom that you started in. " \
						   "It doesn't look like anyone has been in here since you left, " \
						   "although it's hard to be sure. ", 
			  'longDesc': "You find yourself in what appears to be the master bedroom. " \
						  "Behind you is the window you entered in, " \
						  "although it probably won't be too useful without your ladder! " \
						  "There is a closet in front of you and a door to the south of the room. " \
						  "There's a nightstand next to the closet as well. " \
						  "An open door on the north side of the room reveals the master bathroom. Pretty nice if you ask me!\n" \
						  "You're kinda stuck here right now. The window isn't really an option " \
						  "to leave through, so your only option is to somehow be a part of the party. ", 
			  'noClothingDescAppend': "You're dressed as a burglar, so that's obviously not going to work. " \
									  "There's got to be a way to change your appearance.",
				'initialized': False}


doors = {'north': 'masterBathDoor'}

items = ['closet', 'nightstand']

		

masterBedroom = MasterBedroom(aliases, properties, doors, items)
eng.setupRoom(masterBedroom)
eng.goToRoom(masterBedroom) # This line only because the master bedroom is the first room 