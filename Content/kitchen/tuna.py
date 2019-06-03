import eng

class Tuna:
	name = 'tuna'
	visible = False 
	aliases = ['whole tuna', 'fish']
	descriptions = {'desc': "It is a whole small tuna. Sashimi grade! ",
					'takeTuna': "You take the whole tuna. ",
					'giveTuna': "You give the sharks the tuna, They attack it viciously. Hope that kills their appetite. ",
					'nothingToGive': "No one in their right mind would want a whole tuna like this. No human, that is. ",
					'eat': "You're a fan of sushi, but you would have to bite through the skin. Are you sure this is what you want?",
					'aBite': "Okay, one bite. Someone... or something... else might want it. ",
					'alreadyHave': "You already have the tuna",
					'droppedTuna': "You have dropped the tuna. It will smell eventually. ",
					'dontHave': "You don't have the tuna to drop. "}
	properties = {'triedEat': False, 'have': False}
	

	def look(self):
		return self.descriptions['desc']
		
	
	def take(self):
		if self.properties['have'] == False:
			self.properties['have'] = True
			eng.addToInventory(self)
			return self.descriptions['takeTuna']
		else:
			return self.descriptions['alreadyHave']
	
	# drop the tuna, if player is has it 
	def drop(self):
		if self.properties['have'] == False:
			return self.descriptions['dontHave']
		else:
			self.properties['have'] = False
			eng.removeFromInventory(self)
			eng.dropItem(self)
			return self.descriptions['droppedTuna']
	
	# give tuna to hungry leopard sharks	
	def give(self, item):
		#check if item is leopard sharks
		if item is None:
			return "Give it to whom?"
		if item.name == 'sharks':
			eng.removeFromInventory(self)
			item.properties['hungry'] = False	
			return self.descriptions['giveTuna']
		return self.descriptions['nothingToGive']

	def eat(self):
		if self.properties['triedEat'] == False:
			self.properties['triedEat'] = True
			return self.descriptions['eat']
		else:
			return self.descriptions['aBite']

tuna = Tuna()
eng.setupItem(tuna)
