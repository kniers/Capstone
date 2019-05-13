import eng

class FountainPen:
	name = 'fountain pen'
	#type = 'Item'
	visible = False 
	aliases = []
	descriptions = {'desc': "It's a fountain pen. It's completely dry, and the ink must be locked in the desk.",
					'takeFP': "You take the pen. You'll need some ink to use it, but you're otherwise prepared to write your life story.",
					'alreadyTakenFP': "You put the pen down and pick it back up again.",
					'touchFP': "You touch the pen. It feels smooth.",
					'eatFP': "You raise the pen to your mouth, but realize that a puncture wound in your throat probably wouldn't make your mission any easier.",
					'useFPnoInk': "The pen isn't much good without any ink.",
					'useFPwithInk': "FIXME: i dunno",
					'dropNoHold': "You pick up the pen and put it back down. That wasn't very satisfying.",
					'drop': "You put down the pen."}
	properties = {'hasInk': False}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		if eng.inInventory(self):
			return self.descriptions['alreadyTakenFP']
		else:
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['takeFP']


	def touch(self):
		return self.descriptions['touchFP']


	def eat(self):
		return self.descriptions['eatFP']


	def use(self):
		return self.descriptions['useFPnoInk']


	def drop(self):
		if eng.inInventory(self) == False:
			return self.descriptions['dropNoHold']
		else:
			eng.removeFromInventory(self)
			currRoom = eng.getCurrentRoom()
			currRoom.addItem('fountain pen')
			return self.descriptions['drop']


fountainPen = FountainPen()
eng.setupItem(fountainPen)