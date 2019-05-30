import eng

class Sharks:
	name = 'sharks'
	#type = 'Item'
	visible = True 
	aliases = ['leopard sharks']
	descriptions = {'desc': "Five leopard sharks swimming around. They look like they are searching for dinner. ",
					'crazy': "Are you nuts! Those are hungry sharks. They aren't likely to eat humans, but you prize your limbs don't you? ",
					'swim':"You get one finger on one of them, but it swims away fast. "}
	properties = {'hungry': True}
	
	
	def look(self):
		return self.descriptions['desc']

	def touch(self):
		currRoom = eng.getCurrentRoom()
		tank = eng.getItemByName('sharktank')
		if self.properties['hungry']:
			return self.descriptions['crazy']
		elif tank.properties['opened'] == False:
			return tank.descriptions['closeDesc']
		else:
			return self.descriptions['swim']

sharks = Sharks()
eng.setupItem(sharks)
