import eng

class Tooth:
	name = 'megalodon tooth'
	#type = 'Item'
	visible = True
	aliases = ['shark tooth', 'tooth']
	descriptions = {'desc': "It is a large megalodon tooth. ",
					'alreadyHave': "You already have the shark tooth. Maybe we should drop it.",
					'takeTooth': "You take the tooth. It is bigger than your hand. ",
					'droppedTooth' : "You drop the shark tooth. ",
					'dontHave': "You can't drop something you don't have.",
					'eatTooth': "Yeah, that isn't happening. ",
					'underTooth': "Under the tooth you see an emerald. ",
					'secretPlans': "Under the tooth you see some papers wrapped in plastic partially burried under the rocks. It must be pretty important if they're hidden in a shark tank!",
					'cant': "Seems like you can't get to it maybe the sharks are hungry or the tank is closed. "}
	properties = {'have': False, 'had':False}

	def look(self):
		return self.descriptions['desc']

	def eat(self):
		return self.descriptions['eatTooth']
	

	def take(self):
		#First time user tries to take the took it is in a closed tank with hungry sharks
		currRoom = eng.getCurrentRoom()
		sharks = eng.getItemByName('sharks')
		tank = eng.getItemByName('sharktank')
		if self.properties['had'] == False and tank.properties['opened'] and sharks.properties['hungry'] == False:
			self.properties['have'] = True
			self.properties['had'] = True 
			eng.addToInventory(self) # adds to inventory and removes from current room 
			
			character = eng.getItemByName('self')
			character.properties['placesOpened'] += 1
			if character.properties['placesOpened'] == 3:
				tank.properties['hasPlans'] = True
				currRoom.items.append('secret plans')
				currRoom.items.remove('emerald')
				return self.descriptions['secretPlans']
			else:
				emerald = eng.getItemByName('emerald')
				emerald.visible = True	
				return self.descriptions['underTooth']
			
		#Must have had the tooth once
		elif self.properties['have'] == False and self.properties['had']:	
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['takeTooth']
		elif self.properties['have']:
			return self.descriptions['alreadyHave']
		else:
			return self.descriptions['cant']
		
		
	# drop the Tooth, if player is has it 
	def drop(self):
		if self.properties['have'] == False:
			return self.descriptions['dontHave']
		else:
			self.properties['have'] = False
			eng.removeFromInventory(self)
			eng.dropItem(self)
			return self.descriptions['droppedTooth']
		
tooth = Tooth()
eng.setupItem(tooth)
