import eng

class Smokers:
	name = 'smokers'
	visible = False 
	aliases = ['guys', 'cigar smokers']
	descriptions = {'firstConversation': "\"Hey there\", says one of the guys. \"Terrible party, right? We'll trade you a cigar if you get us some cake - I think we missed the dessert out here.\"",
					'desc': "There's some smokers over in the corner of the gardens. Not much else to say about them until you go talk to them. ",
					'information': "Not sure if you've heard this from anyone else, but it's rumored that there's a secret room somewhere in the house. I bet this guy has some really valuable stuff in there! ",
					'noGiftConversation': "I see you're back without any cake for us. Why don't you just bring us some cake and then we can talk? ",
					'alreadyWearing': "You're already wearing the suit!"}
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
		
		



smokers = Smokers()
eng.setupItem(smokers)