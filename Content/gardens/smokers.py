import eng

class Smokers:
	name = 'smokers'
	visible = False 
	aliases = ['guys', 'cigar smokers']
	descriptions = {'firstConversation': "\"Hey there\", says one of the guys. \"Terrible party, right? You can join us for a smoke, but only if you can get us some cake - I think we missed the dessert out here.\"",
					'desc': "There's some smokers over in the corner of the gardens. Not much else to say about them until you go talk to them. ",
					'information': "Not sure if you've heard this from anyone else, but it's rumored that there's a secret room somewhere in the house. I bet this guy has some really valuable stuff in there! ",
					'noGiftConversation': "I see you're back without any cake for us. Why don't you just bring us some cake and then we can talk? ",
					'giveCake': "You give the men the cake, and, as promised, receive cigars in return. Big Al will be pleased with some nice Cuban cigars. ",
					'alreadyWearing': "You're already wearing the suit!",
					'nothingToGive': "These guys only want cake - don't try to give them anything else. "}
	properties = {'eating': False, 'taskStarted': False}
	

	def look(self):
		self.visible = True
		return self.descriptions['desc']
	

	def talk(self):
		if self.properties['taskStarted'] == False:
			self.properties['taskStarted'] = True 
			return self.descriptions['firstConversation']
		else:
			# check whether you've already given them food 
			if self.properties['eating']:
				return self.descriptions['information']
			
			# if you have an item they want
			cake = eng.getItemByName('cake')
			if eng.inInventory(cake):
				return self.give(cake)
			else:
				return self.descriptions['noGiftConversation']
		
		
	def give(self, item):
		if item.name == 'cake':
			eng.removeFromInventory(item)
			self.properties['eating'] = True 
			cigars = eng.getItemByName('cigars')
			cigars.visible = True
			eng.addToInventory(cigars)
			return self.descriptions['giveCake']
		
		return self.descriptions['nothingToGive']


smokers = Smokers()
eng.setupItem(smokers)