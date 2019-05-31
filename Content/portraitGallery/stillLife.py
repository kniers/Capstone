import eng

class StillLife:
	name = 'still life'
	#type = 'Item'
	visible = True 
	aliases = []
	descriptions = {'desc': "It's a hyper-realistic still life. It portrays a green table with a pitcher, some grapes, some dead pheasants, a key, and fruit in a bowl on it. It looks almost too real.",
					'takeSL': "It's too big. You'd never get it out of here without arousing suspicion. Also, it's not that valuable anyway.",
					'touchAlone': "You reach out and gently feel the painting.",
					'touchWithKey': " As your finger runs across the key, you feel metal. Somebody stuck a real key to the painting!",
					'touchNotAlone': "You reach a finger out towards the painting. 'Hey! Hey! HEY!' one of the critics shouts. 'Don't touch the art!'",
					'eatSL': "Artists of that period often used pigments made from substances like mercury and arsenic. In other words, this painting might be poisonous."}
	properties = {'hasKey': True}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']


	def take(self):
		return self.descriptions['takeSL']


	def touch(self):
		currRoom = eng.getCurrentRoom()
		criticA = eng.getItemByName('male critic')
		criticB = eng.getItemByName('female critic')
		if "male critic" in currRoom.items or "female critic" in currRoom.items:
			return self.descriptions['touchNotAlone']
		else:
			if self.properties['hasKey']:
				k = eng.getItemByName('strange key')
				k.visible = True
				return self.descriptions['touchAlone'] + self.descriptions['touchWithKey']
			else:
				return self.descriptions['touchAlone']


	def eat(self):
		return self.descriptions['eatSL']
			

stillLife = StillLife()
eng.setupItem(stillLife)
