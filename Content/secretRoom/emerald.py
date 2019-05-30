import eng

class Emerald:
	name = 'emerald'
	#type = 'Item'
	visible = False
	aliases = ['Eye of Ashoka']
	descriptions = {'desc': "It is a beautiful emerald, looks to be about an eight carats. Stunning... ",
					'alreadyHave': "You already have the emerald. Maybe we should drop it.",
					'takeJewel': "Emerald is in your inventory. The Boss is going to be really happy. ",
					'droppedJewel' : "You drop the emerald. ", 
					'dontHave': "You can't drop something you don't have.",
					'huh': "I don't see any gems. ",
					'eatJewel': "Too big, too valuable, and too hard to eat. "}
	properties = {'have': False}

	def look(self):
		if self.visible:
			return self.descriptions['desc']
		else:
			return self.descriptions['huh']

	def eat(self):
		return self.descriptions['eatJewel']
	

	def take(self):
		if self.visible:
			if self.properties['have'] == False:
				eng.addToInventory(self)
				self.properties['have'] = True
				return self.descriptions['takeJewel']
			else:
				return self.descriptions['alreadyHave']
		else:
			return self.descriptions['huh']		
		
	# drop the Emerald, if player is has it 
	def drop(self):
		if self.properties['have'] == False:
			return self.descriptions['dontHave']
		else:
			self.properties['have'] = False
			eng.removeFromInventory(self)
			eng.dropItem(self)
			return self.descriptions['droppedJewel']

		
emerald = Emerald()
eng.setupItem(emerald)
