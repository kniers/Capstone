import eng

class Portraits:
	name = 'portraits'
	#type = 'Item'
	visible = True 
	aliases = []
	descriptions = {'desc': "The former residents of this house stare down disapprovingly at you from above.",
					'takeThem': "There's too many. Besides, you wouldn't want any of these eyesores in your house.",
					'touchThem': "You'd prefer not to.",
					'eatThem': "They look thoroughly unpalatable."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		return self.descriptions['takeThem']


	def touch(self):
		return self.descriptions['touchThem']


	def eat(self):
		return self.descriptions['eatThem']
			

portraits = Portraits()
eng.setupItem(portraits)
