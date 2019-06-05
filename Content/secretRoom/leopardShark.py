import eng

class Sharks:
	name = 'sharks'
	#type = 'Item'
	visible = True 
	aliases = ['leopard sharks']
	descriptions = {'desc': "Five leopard sharks swimming around. They look like they are searching for dinner. ",
					'docileDesc': "Five leopard sharks swimming around. After they ate the tune they seem much more docile. ",
					'crazy': "Are you nuts! Those are hungry sharks. They aren't likely to eat humans, but you prize your limbs don't you? ",
					'swim': "You get one finger on one of them, but it swims away quickly. ",
					'takeSharks': "Nothing draws attention more than somebody carrying a flailing shark though a posh party."}
	properties = {'hungry': True}
	
	
	def look(self):
		if self.properties['hungry']:
			return self.descriptions['desc']
		else:
			return self.descriptions['docileDesc']

	def touch(self):
		currRoom = eng.getCurrentRoom()
		tank = eng.getItemByName('sharktank')
		if self.properties['hungry']:
			return self.descriptions['crazy']
		elif tank.properties['opened'] == False:
			return tank.descriptions['closedDesc']
		else:
			return self.descriptions['swim']
	
	def hit(self):
		return self.touch()

	def kill(self):
		return self.touch()

	def take(self):
		return self.descriptions['takeSharks']

sharks = Sharks()
eng.setupItem(sharks)
