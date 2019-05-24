import eng 

class Office:
	name = 'Office'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the office again. There's still a desk and all that kinda stuff. ", 
					'longDesc': "The door leads you to what looks like an office. There's a desk with a fountain pen and a letter opener on it. " \
								"There's also a filing cabinet in the corner. The room is windowless, and the only exit is back north through the door you came in. "}
	doors = {'north': 'officeDoor'}
	items = ['desk', 'letter opener', 'fountain pen', 'filing cabinet', 'top drawer', 'bottom drawer', 'blueprints', 'gold statue']
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


office = Office()
eng.setupRoom(office) 