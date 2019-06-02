import eng

class SharkTank:
	name = 'sharktank'
	#type = 'Item'
	visible = True 
	aliases = ['shark tank', 'tank', 'fish tank', 'aquarium']
	descriptions = {'tankDesc': "It is a large shark tank about 18-ft x 24-ft in size. Inside there are five leopard sharks swimming around. The undersea environment has rocks, coral, and various seaweeds. ",
					'openDesc': "You have opened the top of the tank. Inside there are five leopard sharks swimming around. The undersea environment has rocks, coral, and various seaweeds. ",
					'alreadyOpen': "Can't open it twice",
					'closeDesc': "The tank is closed. ",
					'alreadyClosed': "It is closed ",
					'tooth': "You look closer and you notice a huge shark tooth at the bottom in the rocks."}
	properties = {'opened': False, 'hasPlans': False}

	def look(self):
		currRoom = eng.getCurrentRoom()
		if self.properties['opened'] == True:
			description = self.descriptions['openDesc']
		else:
			description = self.descriptions['tankDesc']
		if 'megalodon tooth' in currRoom.items:
			description += self.descriptions['tooth']
		else:
			if self.properties['hasPlans']:
				description += '\n\nThere are some papers wrapped in plastic at the bottom of the tank. Must be something important.'
			elif 'emerald' in currRoom.items:
				description += '\n\nThere is a fine looking emerald at the bottom of the tank. It was covered up by the shark tooth.'
		return description

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
