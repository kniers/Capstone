import eng 

class MasterBathroom:
	name = 'Master Bathroom'
	visited = False
	visible = True # Door to bathroom is open
	aliases = ['master bathroom', 'master bath', 'bathroom']
	descriptions = {'shortDesc': "You're in that master bathroom. Nothing in particular stands out here. " \
								 "It's not like the master bathroom is the most interesting room in the house. ",
					'longDesc': "You've stepped into the master bathroom. It's remarkably clean, compared " \
								"to the disgusting state you leave your own bathroom in at home. There " \
								"doesn't appear to be anything valuable in view, which I guess can be expected. " \
								"There's a vanity sitting between the sink and the bathtub."}
	doors = {'south': 'masterBathDoor'}
	items = ['bathtub', 'sink', 'vanity', 'rubber duck', 'strop'. 'toothpaste']
	properties = {}

			
	def _printShortDesc(self): 
		return self.descriptions['shortDesc']

			
	def _printLongDesc(self):
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
		

masterBathroom = MasterBathroom()
eng.setupRoom(masterBathroom)