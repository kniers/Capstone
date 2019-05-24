import eng

class Landscape:
	name = 'landscape'
	#type = 'Item'
	visible = True 
	aliases = []
	descriptions = {'desc': "It's a sweeping landscape of some European locale.",
					'takeLS': "This thing is huge. You couldn't carry it even if you wanted to.",
					'touchLS': "You actually really like this one. It would be a shame to ruin it.",
					'eatLS': "You can't eat that."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		return self.descriptions['takeLS']


	def touch(self):
		return self.descriptions['touchLS']


	def eat(self, otherThing):
		return self.descriptions['eatLS']
			

landscape = Landscape()
eng.setupItem(landscape)
