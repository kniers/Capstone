import eng

class Bathtub:
	name = 'bathtub'
	#type = 'Item'
	visible = True 
	aliases = []
	descriptions = {'desc': "It's a white ceramic bathtub. There's a rubber duck sitting near the drain.",
					'takeBT': "It's bolted to the floor. Also, it's a freaking bathtub. How the heck would you carry it?",
					'touchSI': "You touch the bathtub. It's ceramic surface is cool.",
					'eatBT': "No."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		return self.descriptions['takeBT']


	def touch(self):
		return self.descriptions['touchSI']


	def eat(self, otherThing):
		if otherThing is None:
			return self.descriptions['eatBT']

		
bathtub = Bathtub()
eng.setupItem(bathtub)