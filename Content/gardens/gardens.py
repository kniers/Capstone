import eng 

class Gardens:
	name = 'Gardens'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the gardens again. Those guys are STILL standing in the corner smoking cigars. ", 
					'longDesc': "The back door leads you out to the gardens. It's a beautiful night, but everyone seems to care about the bar " \
								"inside more than the gardens outside. Of course, you don't care about the weather or the bar; " \
								"you just want to steal as much as possible. \n" \
								"There are two guys standing at the far end of the gardens smoking cigars. Maybe it's worth talking to them to " \
								"see if they happen to slip up and give you some information about where valuables may be stored in the house?"}
	doors = {'south': 'conservatoryGardensDoor', 'west': 'barGardensDoor'}
	items = ['smokers', 'cigars']
	properties = {'initialized': False}

			
	def _printShortDesc(self): 
		return self.descriptions['shortDesc']

			
	def _printLongDesc(self):
		if self.properties['initialized'] == False:
			self.properties['initialized'] = True
		
		return self.descriptions['longDesc']

		
	def enterRoom(self):
		smokers = eng.getItemByName('smokers')
		smokers.visible = True;
		if (self.visited == True):
			return self._printShortDesc()
		else:
			self.visited = True
			return self._printLongDesc()

			
	# Per game requirements, look should reprint long description 
	def look(self):
		return self._printLongDesc()


gardens = Gardens()
eng.setupRoom(gardens) 