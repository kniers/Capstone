import eng 

class Bar:
	name = 'Bar'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the bar again. People are still enjoying conversation and drinks.", 
					'longDesc': "The door leads you to what looks like a bar. The bar has the look of an old London upscale pub. There are a few people in the room enjoying themselves and a bartender behind the counter. At the bar you see a Catholic Priest."}
	doors = {'west': 'ballroomBarDoor', 'east': 'barGardensDoor', 'south': 'barGalleryDoor'}
	items = ['Catholic Priest', 'bartender']
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


bar = Bar()
eng.setupRoom(bar) 
