import eng

class YamazakiCard:
	name = 'business card'
	#type = 'Item'
	visible = False
	aliases = ['meishi']
	descriptions = {'desc': "Genzo Yamazaki, Chief Operating Officer, Matsui Corp. Yokohama, Japan ",
					'droppedCard': "You dropped the business card. ",
					'alreadyHave': "You already have the business card. ",
					'takeCard': "You have Mr. Yamazaki's business card in inventory. ",
					'dontHave': "You don't have the business card. Can't drop. "}
	properties = {'have':False}
	
	
	def look(self):
		return self.descriptions['desc']

	def take(self):
		if self.properties['have'] == True:
			return self.descriptions['alreadyHave']
		else:
			self.properties['have'] = True 
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['takeCard']
		
	# drop the book , if player is has it 
	def drop(self):
		if self.properties['have'] == False:
			return self.descriptions['dontHave']
		else:
			self.properties['have'] = False
			eng.removeFromInventory(self)
			eng.dropItem(self)
			return self.descriptions['droppedCard']



yamazakiCard = YamazakiCard()
eng.setupItem(yamazakiCard)
