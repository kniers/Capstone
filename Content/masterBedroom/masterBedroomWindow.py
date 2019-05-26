import eng

class masterBedroomWindow:
	name = 'masterBedroomWindow'
	visible = True 
	aliases = ['window']
	#roomConnections = {'west': 'Master Bedroom'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this window. " \
							"It would've been your ticket to freedom if you hadn't knocked over the ladder.",
					'noExit': "You can't get out that way without the ladder that you kicked over as you snuck in through the window."}
	properties = {'locked': False}
	
	
	def go(self):
		return self.descriptions['noExit']


	def look(self):
		return self.descriptions['desc']


masterBedroomWindow = masterBedroomWindow()
eng.setupItem(masterBedroomWindow)