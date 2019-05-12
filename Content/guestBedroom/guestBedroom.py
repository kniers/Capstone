import eng 

class GuestBedroom:
	name = 'Guest Bedroom'
	visited = False
	visible = False 
	aliases = []
	descriptions = {'shortDesc': "You're in the guest bedroom again. There's nothing here. ", 
					'longDesc': "You're in the guest bedroom, presumably. It's smaller than the master bedroom. "} 
	doors = {'east': 'guestBedDoor'}
	items = []
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


guestBed = GuestBedroom()
eng.setupRoom(guestBed) 