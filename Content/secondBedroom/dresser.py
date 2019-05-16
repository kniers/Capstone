import eng

class Dresser:
	name = 'dresser'
	#type = 'Item'
	visible = True 
	aliases = []
	descriptions = {'desc': "It's a dresser with three doors and 8-inch long legs. There's a mousetrap sitting under it.",
					'takeDresser': "It's waaaay to heavy.",
					'touchDresser': "You touch the dresser. Good job, now your fingerprints are on it.",
					'eatDresser': "17th Century colonial isn't really on your diet right now.",
					'openDresser': "You check all the drawers to the dresser. There's nothing inside. Apparently nobody's sleeping in here tonight."}
	properties = {'sample': True}
	
	
	def look(self):
		self.visible = True
		currRoom = eng.getCurrentRoom()
		mTrap = eng.getItemByName('mousetrap')
		if mTrap is not None:
			mTrap.visible = True
		return self.descriptions['desc']
	
	
	def take(self): 
		return self.descriptions['takeDresser']


	def touch(self):
		return self.descriptions['touchDresser']


	def eat(self):
		return self.descriptions['eatDresser']


	def open(dresser):
		return self.descriptions['openDresser']

			

dresser = Dresser()
eng.setupItem(dresser)