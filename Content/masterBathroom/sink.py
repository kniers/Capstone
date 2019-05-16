import eng

class Sink:
	name = 'sink'
	#type = 'Item'
	visible = True 
	aliases = []
	descriptions = {'desc': "It's a sink. Whatever.",
					'touchSI': "You wash your hands. Best not to spread disease if you can help it."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']


	def touch(self):
		return self.descriptions['touchSI']
			

sink = Sink()
eng.setupItem(sink)