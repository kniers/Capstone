import eng 

class Conservatory:
	name = 'Conservatory'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the conservatory again. ", 
					'longDesc': "The door leads you to what looks like a conservatory with floor to ceiling windows. You can hear the commotion of people having a good time out in the gardens, but nothing is going on in here. There's a man sitting by himself at the table looking out the window. A highball glass is on the table next to him. "}
	doors = {'north': 'conservatoryGardensDoor', 'west': 'billiardRoomConservatoryDoor'}
	items = ['craftsman', 'billiardTableTopic', 'conservatory windows', 'highball glass', 'mahogany table']
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


conservatory = Conservatory()
eng.setupRoom(conservatory) 