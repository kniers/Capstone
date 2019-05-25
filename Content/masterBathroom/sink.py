import eng

class Sink:
	name = 'sink'
	#type = 'Item'
	visible = True 
	aliases = []
	descriptions = {'desc': "It's a sink. Whatever.",
				'touchSI': "You wash your hands. Best not to spread disease if you can help it.",
				'hitSink': "You punch the sink as hard as you can. OUCH! That hurt.",
				'openSink': "You turn on the water to the sink. This will raise the owner's water bill, giving Big Al a slight budgetary advantage.",
				'alreadyOpen': "You already did that."}
	properties = {'open': False}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']


	def open(self):
		if self.properties['open']:
			return self.descriptions['alreadyOpen']
		else:
			self.properties['open'] = True
			return self.descriptions['openSink']


	def touch(self):
		return self.descriptions['touchSI']


	def use(self):
		return self.descriptions['useSI']


	def kill(self):
		return self.descriptions['hitSink']


	def hit(self):
		return self.descriptions['hitSink']
			

sink = Sink()
eng.setupItem(sink)