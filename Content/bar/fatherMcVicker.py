import eng

class FatherMcVicker:
	name = 'Catholic Priest'
	#type = 'Item'
	visible = True 
	aliases = ['Father McVicker', 'priest', 'father']
	descriptions = {'desc': "There is a Catholic Priest standing at the bar. Looks like he is debating whether to buy a drink or not.",
					'bless':'Father touches you on the shoulder. "Bless you son."',
					'converse':"Ello, I am Father McVicker. Nice to meet you. I have been a friend of this family for three generations.",
					'kingJames': "Did yah know? This house has an original King James Bible in the study. It is a beautiful peace of craftsmanship. You should go check it out. God bless ya laddie. This is turing into quite the party.",
					'offerDrink': "You offer him a drink...\nI really shouldn't. I have been trying to stop... But, it is a party after all. Get me some Scotch on the rocks lad...",
					'preach': "Ill-gotten treasures have no lasting value, but righteousness delivers from death..."}
	properties = {'drinking':False, 'conversation':False}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']

	def talk(self):
		if self.properties['drinking']:
			return self.descriptions['kingJames']
		elif self.properties['conversation']:
			self.properties['drinking'] = True
			return self.descriptions['offerDrink']	
		else:
			self.properties['conversation'] = True
			return self.descriptions['converse']

	def touch(self):
		return self.descriptions['bless']

fatherMcVicker = FatherMcVicker()
eng.setupItem(fatherMcVicker)
