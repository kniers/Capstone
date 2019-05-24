import eng

class PinkFlowers:
	name = 'pink flower'
	#type = 'Item'
	visible = True
	aliases = ['flowers', 'flower', 'pink flowers']
	descriptions = {'desc': "It's a pink flower growing on a bush. It's the kind of flower you'd stick on your formalwear to add a little color.",
					'takePF': "You won't just take one, but you can wear one if you want.",
					'touchPF': "You touch a flower. It's very healthy.",
					'eatPF': "You have a pollen allergy.",
					'dropNoHold': "You have to pick it up before you can drop it.",
					'dropPF': "You drop the flower.",
					'wearPF': "You slide the flower into a convenient notch in your clothing.",
					'alreadyWearing': "You're already wearing one of those.",
					'removeNotWearing': "You have to wear it before you can take it off.",
					'remove': "You take off the flower and drop it on the floor."}
	properties = {'wearing': False}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		return self.descriptions['takePF']


	def touch(self):
		return self.descriptions['touchPF']


	def drop(self):
		if eng.inInventory(self) == False:
			return self.descriptions['dropNoHold']
		else:
			eng.dropItem(self)
			self.properties['wearing'] = False;
			return self.descriptions['dropPF']


	def eat(self):
		return self.descriptions['eatPF']


	def wear(self):
		if self.properties['wearing'] == False:
			self.properties['wearing'] = True 
			eng.addToInventory(self) # adds to inventory and removes from current room
			eng.
			return self.descriptions['wearPF']
		else:
			return self.descriptions['alreadyWearing']
		

	def remove(self):
		if self.properties['wearing'] == False:
			return self.descriptions['removeNotWearing']
		else:
			self.properties['wearing'] = False
			eng.dropItem(self)
			return self.descriptions['remove']
	

pinkFlower = PinkFlower()
eng.setupItem(pinkFlower)