import eng

class LetterOpener:
	name = 'letter opener'
	#type = 'Item'
	visible = True
	aliases = []
	descriptions = {'desc': "It's a letter opener. People with short fingernails use it to open letters. ",
					'sharpDesc': "It looks sharp enough to kill someone with.",
					'takeLO': "You take the letter opener. No envelope will stand in your way now!",
					'alreadyTakenLO': "You already took that.",
					'touchLO': "You touch the letter opener. It's not very sharp, but will do in a pinch.",
					'eatLO': "You raise the letter opener to your mouth, but realize that a puncture wound in your throat probably wouldn't make your mission any easier.",
					'dropNoHold': "You're not even carrying that.",
					'drop': "You put down the letter opener.",
					'sharpenFailLO': "You'll need something to sharpen that with.",
					'sharpenWrongLO': "That won't work.",
					'sharpenSuccessLO': "You sharpen the letter opener. Now you're ready to go postal on the post."}
	properties = {'sharp': False}
	
	
	def look(self):
		self.visible = True
		description = self.descriptions['desc']
		if self.properties['sharp']:
			description += self.descriptions['sharpDesc']
		return description
	
	
	def take(self):
		if eng.inInventory(self):
			return self.descriptions['alreadyTakenLO']
		else:
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['takeLO']


	def touch(self):
		return self.descriptions['touchLO']


	def eat(self):
		return self.descriptions['eatLO']


	def drop(self):
		if eng.inInventory(self) == False:
			return self.descriptions['dropNoHold']
		else:
			eng.removeFromInventory(self)
			eng.dropItem(self)
			return self.descriptions['drop']


	def sharpen(self, otherThing):
		if otherThing is None:
			strop = eng.getItemByName('strop')
			if eng.inInventory(strop):
				self.properties['sharp'] = True 
				return self.descriptions['sharpenSuccessLO']
			return self.descriptions['sharpenFailLO']
		elif otherThing.name == 'strop':
			self.properties['sharp'] = True
			return self.descriptions['sharpenSuccessLO']
		else:
			return self.descriptions['sharpenWrongLO']
			

letterOpener = LetterOpener()
eng.setupItem(letterOpener)