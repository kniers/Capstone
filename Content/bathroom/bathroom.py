import eng 

class Bathroom:
	name = 'Bathroom'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the bathroom off of the ballroom again. " \
								 "There's the window on the outside wall (that window obviously hasn't moved anywhere), " \
								 "but no other exit besides the east door you came in. ", 
					'longDesc': "You're in the bathroom. It's quite spacious, so you look for another exit. " \
								"There's a window to the west, but other than that it looks like the door you came in is the only exit. " \
								"The only thing out of the ordinary is a purse sitting in the corner. ",
					'purseDesc': "The purse is still sitting there as well."}
	doors = {'east': 'ballroomBathroomDoor'}
	items = ['purse', 'bathroomWindow']
	properties = {'initialized': False}

			
	def _printShortDesc(self): 
		purse = eng.getItemByName('purse')
		if eng.inInventory(purse):
			return self.descriptions['shortDesc']
		else: 
			return self.descriptions['shortDesc'] + self.descriptions['purseDesc']

			
	def _printLongDesc(self):
		if self.properties['initialized'] == False:
			self.properties['initialized'] = True
		
		return self.descriptions['longDesc']

		
	def enterRoom(self):
		if (self.visited == True):
			return self._printShortDesc()
		else:
			self.visited = True
			purse = eng.getItemByName('purse')
			purse.visible = True 
			window = eng.getItemByName('bathroomWindow')
			window.visible = True 
			return self._printLongDesc()

			
	# Per game requirements, look should reprint long description 
	def look(self):
		return self._printLongDesc()


bathroom = Bathroom()
eng.setupRoom(bathroom) 