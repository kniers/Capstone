class MasterBedroom:
	def __init__(self, name, aliases, shortDesc, longDesc, doorsToAdd, itemsToAdd):
		self.name = name 
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
	def _printShortDesc(self, gameState): 
		return self.shortDesc
	
	# Can be overridden by child classes so that long description can be dynamic based on state of items	
	def _printLongDesc(self, gameState):
		return self.longDesc
		
	def enterRoom(self, gameState):
		if (self.visited == True):
			return self._printShortDesc(gameState)
		else:
			self._setVisited()
			return self._printLongDesc(gameState)
	
	# Per game requirements, look should reprint long description 
	def look(self, gameState):
		return self._printLongDesc(gameState)
	
	def addItem(self, item):
		self.items.append(item)
		return True
		
	def removeItem(self, itemToRemove):
		try:
			self.items.remove(itemToRemove)
			return True 
		except ValueError: #throws ValueError if item doesn't exist in list
			return False 
	
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
		
	# These are better handled by the engine imo 
	#def getItemByName():
	#def getItemByAlias():
	#def getDoorByName():
	#def getDoorByAlias():


# TESTING
'''
name = "Master Bedroom"
aliases = ["master bed", "bedroom"]
shortDesc = "You're back in the bedroom that you started in.\n" \
			"It doesn't look like anyone has been in here since you left,\n" \
			"although it's hard to be sure.\n"
longDesc = "You find yourself in what appears to be the master bedroom.\n" \
			"Behind you is the window you entered in,\n" \
			"although it probably won't be too useful without your ladder!\n" \
			"There is a closet in front of you and a door to the left.\n" \
			"An open door to the right reveals the master bathroom. Pretty nice if you ask me!\n" \
			"You're kinda stuck here right now. The window isn't really an option\n" \
			"to leave through, so your only option is to somehow be a part of the party.\n" \
			"You're dressed like a burglar, so that's not going to work either.\n" \
			"There's got to be a way to sneak out or a way to change your appearance!\n"
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