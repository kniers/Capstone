import eng

class DancingCouple:
	name = 'dancing couple'
	#type = 'Item'
	visible = True 
	aliases = ['rick', 'ashley']
	descriptions = {'desc': "Two lovebirds are dancing in the center of the room. They only have eyes for each other.",
					'takeRA': "They seem taken enough with each other.",
					'touchRA': "That seems inappropriate.",
					'eatRA': "Ew, no.",
					'talkRA': "Rick: 'I love you!'\n\nAshley: 'I love you too!'\n\n'Rick: 'I'm never gonna give you up!'\n\nAshley: 'I'll never let you down!'\n\nThey dance on, ignoring you.",
					'killRA': "Death cannot stop true love. All it can do is delay it for a while.",
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
			

dancingCouple = DancingCouple()
eng.setupItem(dancingCouple)
