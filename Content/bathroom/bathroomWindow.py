import eng

class BathroomWindow:
	name = 'bathroomWindow'
	visible = False 
	aliases = ['window']
	descriptions = {'desc': "There's a small window on the outside wall of the bathroom. Could this be an escape route?",
					'noExit': "You go to climb through the window, but notice that you're in full view of the front porch once you open it. " \
							  "You definitely can't get out this way without making a scene. You're dressed for the party anyways, so why not just walk out " \
							  "the front door when you've collected enough loot?"}
	properties = {}
	
	
	def go(self):
		return self.descriptions['noExit']


	def look(self):
		return self.descriptions['desc']


bathroomWindow = BathroomWindow()
eng.setupItem(bathroomWindow)