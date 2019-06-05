import eng

class Bathtub:
	name = 'bathtub'
	#type = 'Item'
	visible = True 
	aliases = ['tub', 'bath tub']
	descriptions = {'desc': "It's a white ceramic bathtub. There's a rubber duck sitting near the drain.",
					'takeBT': "It's bolted to the floor. Also, it's a freaking bathtub. How the heck would you carry it?",
					'touchBT': "You touch the bathtub. Its ceramic surface feels cool.",
					'eatBT': "No.",
					'useBT': "You took a shower this morning.",
					'talkBT': "'So what's up?' you say to the bathtub. The bathtub doesn't respond."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		currRoom = eng.getCurrentRoom()
		rDuck = eng.getItemByName('rubber duck')
		if rDuck is not None:
			rDuck.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		return self.descriptions['takeBT']


	def talk(self):
		return self.descriptions['talkBT']


	def use(self):
		return self.descriptions['useBT']


	def touch(self):
		return self.descriptions['touchBT']


	def eat(self):
		return self.descriptions['eatBT']

		
bathtub = Bathtub()
eng.setupItem(bathtub)