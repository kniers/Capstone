import eng 

class MasterBedroom:
	name = 'Master Bedroom'
	visited = False
	visible = True 
	aliases = ['master bed', 'bedroom', 'starting bedroom', 'starting room']
	descriptions = {'shortDesc': "You're back in the bedroom that you started in. " \
								 "It doesn't look like anyone has been in here since you left, " \
								 "although it's hard to be sure. ", 
					'longDesc': "You find yourself in what appears to be the master bedroom. " \
								"Behind you is the window you entered in, " \
								"although it probably won't be too useful because you accidentally knocked over your ladder on the way in! " \
								"There is a closet to your left and a door on the west wall of the room. " \
								"There's a nightstand next to the closet as well. " \
								"An open door on the north side of the room reveals the master bathroom. Pretty nice if you ask me!\n" \
								"You're kinda stuck here right now. The window isn't really an option " \
								"to leave through, so your only option is to somehow be a part of the party. ", 
					'noClothingDescAppend': "You're dressed as a burglar, so that's obviously not going to work. " \
											"There's got to be a way to change your appearance."}
	doors = {'north': 'masterBathDoor', 'west': 'masterBedDoor'}
	items = ['closet', 'nightstand', 'suit', 'gown', 'spare key', 'masterBedroomWindow']
	properties = {'initialized': False}

			
	def _printShortDesc(self): 
		return self.descriptions['shortDesc']

		
	# Dynamic based on what player is wearing 	
	def _printLongDesc(self):
		if self.properties['initialized'] == False:
			self.properties['initialized'] = True
			desc = self.descriptions['longDesc']
			desc += self.descriptions['noClothingDescAppend']
			return desc

		desc = self.descriptions['longDesc']
		suit = eng.getItemByName('suit')
		gown = eng.getItemByName('gown')
		
		if eng.inInventory(suit):
			desc += suit.descriptions['wearingDesc']
		elif eng.inInventory(gown):
			desc += gown.descriptions['wearingDesc']
		else:
			desc += self.descriptions['noClothingDescAppend']
		
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
	

masterBedroom = MasterBedroom()
eng.setupRoom(masterBedroom)
eng.goToRoom(masterBedroom) # This line only because the master bedroom is the first room 
