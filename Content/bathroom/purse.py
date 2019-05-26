import eng

class Purse:
	name = 'purse'
	visible = False 
	aliases = ['clutch']
	descriptions = {'desc': "The purse is just laying there. Someone must have left it there by accident.",
					'take': "You pick up the purse. ",
					'pocketSuit': "It looks weird for you to be carrying a purse, but, luckily, it's small enough to slip into the inside pocket of your suit.",
					'purseGown': "It happens to match the gown you're wearing, so you shouldn't be too conspicuous walking around with it.",
					'open': "You open the purse to have a rummage around inside. Surprisingly, there isn't anything obviously valuable. The purse itself is " \
							"designer, though, so it still may be worth taking it to sell on the black market."}
	properties = {}
	

	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		eng.addToInventory(self)
		suit = eng.getItemByName('suit')
		if eng.inInventory(suit):
			return self.descriptions['take'] + self.descriptions['pocketSuit']
		else:
			return self.descriptions['take'] + self.descriptions['purseGown']
		
		
	def open(self):
		return self.descriptions['open']


purse = Purse()
eng.setupItem(purse)