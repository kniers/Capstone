import eng

class FilingCabinet:
	name = 'filing cabinet'
	#type = 'Item'
	visible = True 
	aliases = ['cabinet']
	descriptions = {'desc': "It's a filing cabinet. There are two drawers, one above the other.",
					'takeFC': "You would certainly hurt your back trying to carry that around, and Big Al wants healthy backs for his minions.",
					'touchFC': "boop",
					'eatFC': "It's too tough to chew.",
					'openFC': "Top drawer or bottom drawer?"}
	properties = {}
	
	
	def look(self):
		self.visible = True
		tDrawer = eng.getItemByName('top drawer')
		if tDrawer is not None:
			tDrawer.visible = True
		bDrawer = eng.getItemByName('bottom drawer')
		if bDrawer is not None:
			bDrawer.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		return self.descriptions['takeFC']


	def touch(self):
		return self.descriptions['touchFC']


	def open(self):
		tDrawer = eng.getItemByName('top drawer')
		if tDrawer is not None:
			tDrawer.visible = True
		bDrawer = eng.getItemByName('bottom drawer')
		if bDrawer is not None:
			bDrawer.visible = True
		return self.descriptions['openFC']


	def eat(self, otherThing):
		return self.descriptions['eatFC']
			

filingCabinet = FilingCabinet()
eng.setupItem(filingCabinet)