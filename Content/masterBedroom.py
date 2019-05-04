import eng 

class MasterBedroom:
	name = "Master Bedroom"
	
	def __init__(self, name, aliases, shortDesc, longDesc, doorsToAdd, itemsToAdd):
		self.visited = False 
		self.aliases = aliases 
		self.shortDesc = shortDesc 
		self.longDesc = longDesc
		self.doors = {}
		self.doors.update(doorsToAdd)
		self.items = []
		for itemToAdd in itemsToAdd:
			self.items.append(itemToAdd)
	
	def _setVisited(self):
		self.visited = True 
		
	def isAlias(self, alias):
		if alias in self.aliases:
			return True
		else:
			return False 
	
	# Can be overridden by child classes so that short description can be dynamic based on state of items
	def _printShortDesc(self): 
		return self.shortDesc
	
	# Can be overridden by child classes so that long description can be dynamic based on state of items	
	def _printLongDesc(self):
		wearingSuitDesc = "You're dressed in a suit, so you're safe to go into the party - just don't act weird."
		noClothing = "You're dressed as a burglar, so that's not going to work. " \
					"There's got to be a way to change your appearance."
		desc = self.longDesc
		if eng.inInventory('suit'):
			desc += wearingSuitDesc
		else:
			desc += noClothing
		
		return desc
		
	def enterRoom(self):
		if (self.visited == True):
			return self._printShortDesc()
		else:
			self._setVisited()
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
	
	'''
	def itemInRoom(self, item):
		try:
			idx = self.items.index(item)
			return True 
		except ValueError: #throws ValueError if item doesn't exist in list
			return False 
	
	def doorInRoom(self, door):
		for direction in self.doors:
			if self.doors[direction] == door:
				return True
		return False
	'''


		
name = "Master Bedroom"
aliases = ['master bed', 'bedroom', 'starting bedroom']
shortDesc = "You're back in the bedroom that you started in. " \
			"It doesn't look like anyone has been in here since you left," \
			"although it's hard to be sure. "
longDesc = "You find yourself in what appears to be the master bedroom. " \
			"Behind you is the window you entered in, " \
			"although it probably won't be too useful without your ladder! " \
			"There is a closet in front of you and a door to the left. " \
			"There's a nightstand next to the closet as well. " \
			"An open door to the right reveals the master bathroom. Pretty nice if you ask me! " \
			"You're kinda stuck here right now. The window isn't really an option " \
			"to leave through, so your only option is to somehow be a part of the party. "
#doors = {'North': 'Master Bathroom Door', 'South': 'Master Bedroom Door', 'West': 'Bedroom Window'}
doors = {}
items = ['closet', 'nightstand']

		

MasterBedroom = MasterBedroom("", aliases, shortDesc, longDesc, doors, items)
eng.setupRoom(MasterBedroom)
print(eng.goToRoom(MasterBedroom)) # This line only because the master bedroom is the first room 
	
	
# TESTING
'''
name = "Master Bedroom"
aliases = ["master bed", "bedroom"]
shortDesc = "You're back in the bedroom that you started in." \
			"It doesn't look like anyone has been in here since you left," \
			"although it's hard to be sure."
longDesc = "You find yourself in what appears to be the master bedroom." \
			"Behind you is the window you entered in," \
			"although it probably won't be too useful without your ladder!" \
			"There is a closet in front of you and a door to the left." \
			"An open door to the right reveals the master bathroom. Pretty nice if you ask me!" \
			"You're kinda stuck here right now. The window isn't really an option" \
			"to leave through, so your only option is to somehow be a part of the party." \
			"You're dressed like a burglar, so that's not going to work either." \
			"There's got to be a way to sneak out or a way to change your appearance!"
doors = {'North': 'Master Bathroom Door', 'South': 'Master Bedroom Door'}
items = ['suit']			
firstRoom = MasterBedroom(name, aliases, shortDesc, longDesc, doors, items)

print(firstRoom.enterRoom("NULL"))
if (firstRoom.visited == True):
	print("enterRoom sets firstRoom to visited correctly\n")
print(firstRoom.enterRoom("NULL"))
print(firstRoom.look("NULL"))

print("'master bed' is alias: " + str(firstRoom.isAlias("master bed")))
print("'notAnAlias' is alias: " + str(firstRoom.isAlias("notAnAlias")))
print("")

if (firstRoom.doorInRoom("Master Bathroom Door") == True):
	print("There is a bathroom door in the room")
if (firstRoom.doorInRoom("Closet") == False):
	print("There isn't a closet in the room")

if (firstRoom.itemInRoom("suit") == True):
	print("\nThere is a suit in the room")
if (firstRoom.itemInRoom("notInRoom") == False):
	print ("Item not in room works correctly")

print("Baseball in room: " + str(firstRoom.itemInRoom("baseball")) + "\n")
firstRoom.addItem("baseball")
print("Baseball in room: " + str(firstRoom.itemInRoom("baseball")) + "\n")
firstRoom.removeItem("baseball")
print("Baseball in room: " + str(firstRoom.itemInRoom("baseball")) + "\n")
'''