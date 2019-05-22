import eng

class Cake:
	name = 'cake'
	visible = False 
	aliases = []
	descriptions = {'desc': "It's cake. It's got all the fancy stuff that cake people do with the frosting. Looks pretty tasty. ",
					'takeCake': "You pick up a few slices, as much as you can hold. ",
					'giveDesc': "Give to who? Try \"give cake to __________\" "}
	properties = {}
	

	def look(self):
		self.visible = True
		return self.descriptions['desc']
		
	
	def take(self):
		eng.addToInventory(self)
		return self.descriptions['takeCake']
	
		
	def give(self, item):
		return self.descriptions['giveDesc']


cake = Cake()
eng.setupItem(cake)