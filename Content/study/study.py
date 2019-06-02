import eng 

class Study:
	name = 'Study'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the study again. Same desk along the wall as before. The only exit seems to be the one to the east you came in. ", 
					'longDesc': "The door leads you to what looks like a study. " \
								"There's a desk along the wall with ample light for getting lost in long periods of study. " \
								"The walls are lined with interesting artifacts from around the world. " \
								"A woman is standing around admiring the artifacts. " \
								"The only exit seems to be the east door you just came in. "}
	doors = {'east': 'libraryStudyDoor'}
	items = ['longDesk', 'Bible', 'margaret', 'beer', 'artifacts', 'mummy\'s curse']
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


study = Study()
eng.setupRoom(study) 
