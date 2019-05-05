import eng 

class MasterBathroom:
	name = "masterBathroom"
	
	def __init__(self, aliases, properties, doorsToAdd, itemsToAdd):
		self.visited = False 
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

			
	def _printLongDesc(self):
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



aliases = ['master bath', 'bathroom']

properties = {'shortDesc': "You're in that master bathroom. Nothing in particular stands out here. " \
						   "It's not like the master bathroom is the most interesting room in the house. ",
			  'longDesc': "You've stepped into the master bathroom. It's remarkably clean, compared " \
						  "to the disgusting state you leave your own bathroom in at home. There " \
						  "doesn't appear to be anything valuable in view, which I guess can be expected. " \
						  "Outside of possibly some jewelry, what would you really expect to find in a bathroom?"}


doors = {'south': 'masterBathDoor'}

items = []

		

masterBathroom = MasterBathroom(aliases, properties, doors, items)
eng.setupRoom(masterBathroom)