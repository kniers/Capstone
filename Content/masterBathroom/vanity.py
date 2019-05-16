import eng

class vanity:
	name = 'vanity'
	#type = 'Item'
	visible = True 
	aliases = []
	descriptions = {'desc': "It's a vanity, a small table for preparing one's self in the morning. There's a drawer that you can open.",
					'touchVanity': "You touch the vanity. Nothing happens.",
					'openVanity': "You open the drawer to the vanity. There's a strop inside as well as a bunch of useless crap."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']


	def touch(self):
		return self.descriptions['touchSI']


	def open(self):
		return self.descriptions['openVanity']
			

vanity = Vanity()
eng.setupItem(vanity)