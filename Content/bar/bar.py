import eng 

class Bar:
	name = 'Bar'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the bar again. People are still enjoying conversation and drinks. There are exits to the south and west, and a door to the east leading outside. ", 
					'longDesc': "The door leads you to a bar. " \
								"The bar has the look of an old London upscale pub with a long marble counter. " \
								"There are a few people in the room enjoying themselves and a bartender behind the counter. " \
								"At the bar you see a Catholic Priest. Once you're done here, you can take west or south exits, " \
								"or a door to the east that leads outside. "}
	doors = {'west': 'ballroomBarDoor', 'east': 'barGardensDoor', 'south': 'barGalleryDoor'}
	items = ['Catholic Priest', 'bartender', 'counter', 'bone key']
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
			gardens = eng.getRoomByName('Gardens')
			gardens.visible = True # Bar description talks about outside, so it should be labeled visible 
			return self._printLongDesc()

			
	# Per game requirements, look should reprint long description 
	def look(self):
		return self._printLongDesc()


bar = Bar()
eng.setupRoom(bar) 
