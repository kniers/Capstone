import eng

class Cake:
	name = 'cake'
	visible = False 
	aliases = []
	descriptions = {'desc': "It's cake. It's got all the fancy stuff that cake people do with the frosting. Looks pretty tasty. ",
					'takeCake': "You pick up a few slices, as much as you can hold. There's still plenty more in the fridge. ",
					'giveCake': "You give the men the cake, and, as promised, receive cigars in return. Big Al will be pleased with some nice Cuban cigars. ",
					'wrongPerson': "They politely decline the cake. Maybe someone else wants it. "}
	properties = {}
	

	def look(self):
		self.visible = True
		return self.descriptions['desc']
		
	
	def take(self):
		if eng.inInventory(self):
			return "You already have some cake."
		else:
			eng.addToInventory(self)
			currRoom = eng.getCurrentRoom()
			if currRoom.name == 'Kitchen':
				if not 'cake' in currRoom.items:
					currRoom.items.append('cake')
			return self.descriptions['takeCake']
	
		
	def give(self, item):
		if item is None:
			return "Give it to whom?"
		elif item.name == 'smokers':
			eng.removeFromInventory(self)
			item.properties['eating'] = True 
			cigars = eng.getItemByName('cigars')
			cigars.visible = True
			eng.addToInventory(cigars)
			return self.descriptions['giveCake']
		
		return self.descriptions['wrongPerson']

	def drop(self):
		if eng.inInventory(self):
			currRoom = eng.getCurrentRoom()
			if currRoom.name == 'Kitchen':
				eng.removeFromInventory(self)
				return "You put the cake back in the refrigerator with the rest of it."
			else:
				eng.dropItem(self)
				return "You set the cake down. "
		else:
			return "You're not holding any cake. "

	# Eating removes it from your inventory, but there's an infinite supply in the kitchen
	def eat(self):
		if eng.inInventory(self):
			eng.removeFromInventory(self)
			return "You eat all the cake you were holding. Delicious!"
		else:
			return "You're not holding any cake. "


cake = Cake()
eng.setupItem(cake)