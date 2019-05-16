import eng 

class SecondBedroom:
	name = 'Second Bedroom'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the second bedroom again. ", 
					'longDesc': "The door leads you to another bedroom. There's a mousetrap in the corner. "}
	doors = {'east': 'secondBedDoor'}
	items = ['mousetrap', 'mouse']
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