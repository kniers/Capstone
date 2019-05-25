import eng

class Maid:
	name = 'maid'
	#type = 'Item'
	visible = True 
	aliases = []
	descriptions = {'desc': "The maid is snoring in the corner. She's holding a picture of the butler to her chest and smiling. Probably best not to wake her.",
					'takeMaid': "You mean out to dinner? She's not your type.",
					'touchMaid': "Don't be that guy.",
					'eatMaid': "Don't be a cannibal.",
					'killMaid': "Big Al doesn't want you to Rambo your way through this one. She won't notice you any time soon, so best to leave her.",
					'talkMaid': "You're not supposed to be up here. If the maid sees you, she'll raise the alarm. You probably should let her sleep."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		return self.descriptions['takeMaid']


	def use(self):
		return self.descriptions['touchMaid']


	def touch(self):
		return self.descriptions['touchMaid']


	def eat(self):
		return self.descriptions['eatMaid']


	def kill(self):
		return self.descriptions['killMaid']


	def hit(self):
		return self.descriptions['killMaid']


	def talk(self):
		return self.descriptions['talkMaid']
			

maid = Maid()
eng.setupItem(maid)