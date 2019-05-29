import eng

class Cake:
	name = 'cake'
	visible = False 
	aliases = []
	descriptions = {'desc': "It's cake. It's got all the fancy stuff that cake people do with the frosting. Looks pretty tasty. ",
					'takeCake': "You pick up a few slices, as much as you can hold. ",
					'giveCake': "You give the men the cake, and, as promised, receive cigars in return. Big Al will be pleased with some nice Cuban cigars. ",
					'nothingToGive': "These guys only want cake - don't try to give them anything else. "}
	properties = {}
	

	def look(self):
		self.visible = True
		return self.descriptions['desc']
		
	
	def take(self):
		eng.addToInventory(self)
		return self.descriptions['takeCake']
	
		
	def give(self, item):
		if item.name == 'smokers':
			eng.removeFromInventory(self)
			item.properties['eating'] = True 
			cigars = eng.getItemByName('cigars')
			cigars.visible = True
			eng.addToInventory(cigars)
			return self.descriptions['giveCake']
		
		return self.descriptions['nothingToGive']


cake = Cake()
eng.setupItem(cake)