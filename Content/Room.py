# Room parent class. All actual rooms will inherit from this parent.
class Room:
	def __init__(self):
		self.roomID = 0
		self.visited = 0
		self.name = "Bedroom"
		self.doors = {} #Direction:doorName pairs
		self.items = ["suit"]
		
	def __init__(self, doorsToAdd, itemsToAdd):
		self.visited = 0
		self.doors = {}
		self.doors.update(doorsToAdd)
		self.items = []
		for itemToAdd in itemsToAdd:
			self.items.append(itemToAdd)
	
	def setVisited(self):
		self.visited = 1
		
	def _printShortDesc(self):
		return self.shortDesc
		
	def _printLongDesc(self):
		return self.longDesc
		
	def printDescription(self):
		if (self.visited == 1):
			return self._printShortDesc()
		else:
			self.setVisited()
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
	
		

#room1 = Room()
#print(room1.printDescription())
#room1.setVisited()
#print(room1.printDescription())