import eng

class SittingCouple:
	name = 'sitting couple'
	#type = 'Item'
	visible = True 
	aliases = ['Felix', 'Sara']
	descriptions = {'desc': "",
					'takeRA': "They're happy where they are.",
					'touchRA': "Let's talk personal space.",
					'eatRA': "Just no.",
					'talkRA': "You: 'How are you two doing?'\n\nSara: 'Oh, just dandy. There's nobody here we know, so we just picked a quiet room to chat in.'\n\nFelix: 'We were discussing that statue over there. I think it's an original Rodin, but Sara thinks it's a copy.'",
					'killRA': "If you kill one, the other would call for help. Also, that's kind of a jerk move.",
					'hitRA': "That wouldn't help you in any way. And it might get you arrested.",
					'giveRA': "They don't want anything."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']


	def hit(self):
		return self.descriptions['hitRA']


	def give(self):
		return self.descriptions['giveRA']


	def take(self):
		return self.descriptions['takeRA']


	def kill(self):
		return self.descriptions['killRA']


	def talk(self):
		return self.descriptions['talkRA']


	def touch(self):
		return self.descriptions['touchRA']



	def eat(self):
		return self.descriptions['eatRA']
			

sittingCouple = SittingCouple()
eng.setupItem(sittingCouple)
