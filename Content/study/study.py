import eng 

class Study:
	name = 'Study'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the study again. Same desk long the wall as before.", 
					'longDesc': "The door leads you to what looks like a study. The study has a desk along the wall. There is ample light for getting lost in long peroids of study."}
	doors = {'east': 'libraryStudyDoor'}
	items = ['longDesk', 'Bible']
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
