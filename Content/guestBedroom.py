import eng 

class GuestBedroom:
	name = "Guest Bedroom"
	
	def __init__(self, aliases, properties, doorsToAdd, itemsToAdd):
		self.visited = False 
		self.visible = False 
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
		
		return self.properties['longDesc']

		
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



aliases = []

properties = {'shortDesc': "You're in the guest bedroom again. There's nothing here. ", 
			  'longDesc': "You're in the guest bedroom, presumably. It's smaller than the master bedroom. ",
			  'initialized': False}


doors = {'east': 'guestBedDoor'}

items = []

		

guestBed = GuestBedroom(aliases, properties, doors, items)
eng.setupRoom(guestBed) 