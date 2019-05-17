import eng

class Mousetrap:
	name = 'mousetrap'
	#type = 'Item'
	visible = False 
	aliases = ['trap']
	descriptions = {'desc': "You look more closely at the mousetrap. Hey, there's a mouse inside! Who knew?",
					'takeMT': "The mousetrap's a little too bulky to carry around, but you can take the mouse if you like.",
					'touchMT': "You touch the mousetrap. Nothing happens.",
					'eatMT': "Half of Europe died due to diseases carried by rats. That's a risk you're not taking.",
					'openMT': "You slide open the door to the mousetrap. The mouse inside races toward the opening and right into your open hands. Hey, you got a friend!",
					'openEmpty': "You slide open the door to the mosuetrap. There's nothing inside."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		currRoom = eng.getCurrentRoom()
		mouse = eng.getItemByName('mouse')
		if mouse is not None:
			mouse.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		return self.descriptions['takeMT']


	def touch(self):
		return self.descriptions['touchMT']


	def eat(self):
		return self.descriptions['eatMT']


	def open(self):
		currRoom = eng.getCurrentRoom()
		mouse = eng.getItemByName('mouse')
		if 'mouse' in currRoom.items:
			mouse.visible = True
			eng.addToInventory(mouse) # adds to inventory and removes from current room 
			return self.descriptions['openMT']
		else:
			return self.descriptions['openEmpty']
			
mousetrap = Mousetrap()
eng.setupItem(mousetrap)