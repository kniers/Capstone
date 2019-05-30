import eng

class SharkTank:
	name = 'sharktank'
	#type = 'Item'
	visible = True 
	aliases = ['shark tank', 'tank', 'fish tank', 'aquarium']
	descriptions = {'tankDesc': "It is a large shark tank about 18-ft x 24-ft in size. Inside there are five leopard sharks swimming around. The undersea environment has rocks, coral, and various seaweeds. You look closer and you notice a huge shark tooth at the bottom in the rocks.",
					'openDesc': "You have opened the top of the tank.",
					'alreadyOpen': "Can't open it twice",
					'closeDesc': "The tank is closed. ",
					'alreadyClosed': "It is closed "}
	properties = {'opened': False}

	def look(self):
		if self.properties['opened'] == True:
			return self.description['openDesc']
		else:
			return self.descriptions['tankDesc']

	def open(self):
		if self.properties['opened'] == True:
			return self.descriptions['alreadyOpen']
		else:
			self.properties['opened'] = True
			return self.descriptions['openDesc']

	def close(self):
		if self.properties['opened'] == True:
			self.properties['opened'] = False
			return self.descriptions['closedDesc']
		else:
			return self.descriptions['alreadyClosed']

sharktank = SharkTank()
eng.setupItem(sharktank)
