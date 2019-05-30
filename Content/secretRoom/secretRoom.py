import eng 

class SecretRoom:
	name = 'Secret Room'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the secret room again. Same big shark tank. ", 
					'longDesc': "The door leads you to a secret room. Cool! In the center of the room you see a huge aquarium with what seem to be leopard sharks. "}
	doors = {'up': 'librarySecretRoomDoor'}
	items = ['emerald', 'sharktank', 'sharks', 'megalodon tooth']
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


secretRoom = SecretRoom()
eng.setupRoom(secretRoom) 
