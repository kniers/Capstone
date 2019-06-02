import eng

class Fridge:
	name = 'fridge'
	visible = False 
	aliases = ['refrigerator']
	descriptions = {'openFridge': "Someone (you!?) was irresponsible and left the fridge open. There's so much cake in there, but it's starting to soften. ",
					'openWithTuna': "There's a whole tuna in here, too.",
					'desc': "There's a massive fridge towards the back of the kitchen. It's like one of those super fancy ones that gets " \
							"advertised on TV, but bigger. The owner of this place must be loaded if he wastes money on a fridge that could " \
							"fit an elephant. ",
					'move': "Dude... No... You can't move the fridge in the middle of a busy cocktail party. ",
					'open': "You open the fridge and there's cake... so much cake. There is also a small whole tuna. Take what you need - it doesn't seem like anyone cares. ",
					'closeDoor': "Much better. That cake is safe in the cold fridge now. ",
					'alreadyOpened': "The fridge is already open. Take the cake or close it before it gets warm. ",
					'alreadyClosed': "The fridge is already closed. No need to close it again, whatever that means."}
	properties = {'opened': False}
	

	def look(self):
		self.visible = True
		if self.properties['opened'] == True:
			currRoom = eng.getCurrentRoom()
			if 'tuna' in currRoom.items:
				return self.descriptions['openFridge'] + self.descriptions['openWithTuna']
			else:
				return self.descriptions['openFridge']
		else:
			return self.descriptions['desc']
	

	def move(self):
		return self.descriptions['move']
	
	
	def open(self):
		if self.properties['opened'] == True:
			return self.descriptions['alreadyOpened']
			
		self.properties['opened'] = True
		cake = eng.getItemByName('cake')
		cake.visible = True 
		tuna = eng.getItemByName('tuna')
		tuna.visible = True 
		return self.descriptions['open']
	
	
	def close(self):
		if self.properties['opened']:
			self.properties['opened'] = False
			return self.descriptions['closeDoor']
		else:
			return self.descriptions['alreadyClosed']
		
		


fridge = Fridge()
eng.setupItem(fridge)
