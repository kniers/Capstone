import eng

class RodinLocation:
	name = 'rodin location'
	#type = 'Item'
	visible = False
	aliases = ['rodin clue']
	descriptions = {'desc': "You found a statue by Rodin. You can tell people about where it is if they're interested."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']


rodinLocation = RodinLocation()
eng.setupItem(rodinLocation)
