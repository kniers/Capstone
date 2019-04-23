# Room parent class. All actual rooms will inherit from this parent.
class Room:
	def __init__(self, doorsToAdd, itemsToAdd):
		self.visited = 0
		self.doors = {}
		self.doors.update(doorsToAdd)
		self.items = []
		for itemToAdd in itemsToAdd:
			self.items.append(itemToAdd)
	
	def _setVisited(self):
		self.visited = 1
	
	# Can be overridden by child classes so that short description can be dynamic based on state of items
	def _printShortDesc(self, gameState): 
		return self.shortDesc
	
	# Can be overridden by child classes so that long description can be dynamic based on state of items	
	def _printLongDesc(self, gameState):
		return self.longDesc
		
	def enterRoom(self, gameState):
		if (self.visited == 1):
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