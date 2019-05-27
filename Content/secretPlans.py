import eng

class SecretPlans:
	name = 'secret plans'
	#type = 'Item'
	visible = True 
	aliases = ['plans']
	descriptions = {'desc': "These are the secret plans for MacGuffin Inc's latest product. This is the one thing Big Al wants the most.",
					'takeSP': "You take the plans without any hesitation.",
					'alreadyTakenSP': "You already took that.",
					'touchSP': "You can't believe that they're real, but they are.",
					'dropNoHold': "You can't do that.",
					'drop': "You're not dropping these. This is the one thing Big Al wants most."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		if eng.inInventory(self):
			return self.descriptions['alreadyTakenSP']
		else:
			billiardTable = eng.getItemByName('billiard table')
			billiardTable.properties['hasPlans'] = False
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['takeSP']


	def touch(self):
		return self.descriptions['touchSP']


	def drop(self):
		if eng.inInventory(self) == False:
			return self.descriptions['dropNoHold']
		else:
			return self.descriptions['drop']
			

secretPlans = SecretPlans()
eng.setupItem(secretPlans)
