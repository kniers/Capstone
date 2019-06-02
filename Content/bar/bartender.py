import eng

class Bartender:
	name = 'bartender'
	visible = True 
	aliases = []
	descriptions = {'desc': "The bartender is standing behind the bar, serving drinks to whoever wants them.",
					'touchBT': "You reach out and shake the bartender's hand.",
					'killBT': "You're not going to eliminate any source of free drinks.",
					'hitBT': "You're not going to offend a source of free drinks.",
					'talkBT': "Good evening. I'm sorry, but we just ran out of beer. Maybe there's something else I can make for you."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']


	def hit(self):
		return self.descriptions['hitBT']


	def kill(self):
		return self.descriptions['killBT']


	def touch(self):
		return self.descriptions['touchBT']

	def talk(self):
		return self.descriptions['talkBT']
			

bartender = Bartender()
eng.setupItem(bartender)
