import eng 

class SecondBedroom:
	name = 'Second Bedroom'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the second bedroom again. There are three children talking in the corner. " \
								 "The only exit remains back out east to the hallway. ", 
					'longDesc': "The door leads you to another bedroom. " \
								"The only thing that makes it different from the other bedroom is a dresser in the corner " \
								"and three children playing and talking next to the window. " \
								"The only exit is back out to the hallway to the east."}
	doors = {'east': 'secondBedDoor'}
	items = ['mousetrap', 'mouse', 'dresser', 'children']
	properties = {'initialized': False}

			
	def _printShortDesc(self): 
		return self.descriptions['shortDesc']

			
	def _printLongDesc(self):
		if self.properties['initialized'] == False:
			self.properties['initialized'] = True
		
		return self.descriptions['longDesc']

		
	def enterRoom(self):
		if (self.visited == True):
			return self._printShortDesc()
		else:
			self.visited = True
			return self._printLongDesc()

			
	# Per game requirements, look should reprint long description 
	def look(self):
		return self._printLongDesc()


secondBedroom = SecondBedroom()
eng.setupRoom(secondBedroom) 
