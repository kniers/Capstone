import eng

class Cigars:
	name = 'cigars'
	visible = False 
	aliases = []
	descriptions = {'desc': "Nice Cuban cigars. Big Al will probably enjoy these. "}
	properties = {}
	

	def look(self):
		self.visible = True
		return self.descriptions['desc']
	

cigars = Cigars()
eng.setupItem(cigars)