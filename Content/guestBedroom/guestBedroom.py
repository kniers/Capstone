import eng 

class GuestBedroom:
	name = 'Guest Bedroom'
	visited = False
	visible = False 
	aliases = []
	descriptions = {'shortDescA': "You're in the guest bedroom again. The maid is still asleep in the corner.",
			'shortDescB': "You're in the guest bedroom again. The maid and butler are quietly chatting in the corner. They won't notice you.", 
					'longDescA': "You're in the guest bedroom, presumably. It's smaller than the master bedroom. " \
								 "There's a maid sleeping in the corner with a picture of the butler resting on her chest. " \
								 "The room is windowless ('kinda weird for a bedroom', you think to yourself, but whatever), " \
								 "so the only exit is back out the south door that you entered through.",
					'longDescB': "You're in the guest bedroom, presumably. It's smaller than the master bedroom. " \
								 "The maid and butler are quietly chatting in the corner. They won't notice you. " \
								 "As mentioned, the room is windowless so you're only exit is the door to the south that you entered through. "} 
	doors = {'south': 'guestBedDoor'}
	items = ['maid']
	properties = {'initialized': False, 'maidAsleep': True}

			
	def _printShortDesc(self):
		if self.properties['maidAsleep'] == True:
			return self.descriptions['shortDescA']
		else:
			return self.descriptions['shortDescB']

			
	def _printLongDesc(self):
		if self.properties['initialized'] == False:
			self.properties['initialized'] = True

		if self.properties['maidAsleep']:
			return self.descriptions['longDescA']
		else:
			return self.descriptions['longDescB']

		
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
