import eng

class Butler:
	name = 'butler'
	#type = 'Item'
	visible = True 
	aliases = []
	descriptions = {'descAlive': "The butler is standing at the top of the stairway, observing the party below. You can't sneak past him without arousing his suspicion. You could kill him if you had a weapon, but Big Al would prefer this mission be done quietly.",
					'descDead': "The butler's body is still right where you left it.",
					'descHolding': "You're carrying the butler's body. You should drop it somewhere out of sight.",
					'takeButlerAlive': "You mean, like to dinner? I don't think he'd be interested.",
					'takeButlerDead': "You pick up the butler's body. Now to get it out of sight.",
					'touchButlerAlive': "That would attract his attention, something you don't want at the moment.",
					'touchButlerDead': "You poke the body. Yep, he's definitely dead.",
					'eatButler': "Ew, no.",
					'killButlerUnarmed': "You jump on the butler and begin pummeling him with your fists. He's very spry for his age, and manages to twist out of your grip. As you spar, he calls for help. You hear the sound of footsteps on the stairs. They have guns...\n\nYou snap out of the daydream. That won't work.",
					'killButlerLOFail': "The letter opener isn't very sharp. The butler would call for help before you got him.",
					'killButlerLOSuccess': "You cover the butler's mouth with one hand and stab his neck with the other. Success. You probably should hide the body so they can't track the murder back to Big Al.",
					'killButlerWithMaid': "The butler will be flirting with the maid for a while. Who are you to break up their happiness?",
					'killFail': "That's probably not the best weapon.",
					'killDead': "Stop! Stop! He's already dead!",
					'alreadyTakenButler': "You've already got the body.",
					'dropNoHold': "You have to pick him up before you can drop him.",
					'dropButler': "You place the butler's body in an out-of-the-way corner.",
					'hitButler': "If you hit the butler, he'll raise the alarm. That would be a problem.",
					'talkButler': "If the butler notices you, he'll raise the alarm. That would be a problem.",
					'takeHidden': "It's not worth the trouble to dig the body out from where you've hidden it.",
					'dropOffice': "You open a closet and stick the butler inside. Nobody will find him for a while. Perfect.",
					'dropGuest': "You quietly slip the body under the bed. Hopefully the maid doesn't find it when she wakes up.",
					'dropMaster': "You quietly slip the body under the bed. Mr. Winston will smell it...eventually...",
					'dropSecond': "Probably best not to hide the body with these children around.",
					'dropBathroom': "You stick the body in the bathtub and close the curtain. Mr. Winston will have an unpleasant surprise for his bath tomorrow.",
					'dropHallway': "You drop the body. It's not hidden, though. You need to hide it before you go downstairs."}
	properties = {'dead': False, 'withMaid': False, 'bodyHidden': False}
	
	
	def look(self):
		self.visible = True
		if eng.inInventory(self):
			return self.descriptions['descHolding']
		elif self.properties['dead']:
			return self.descriptions['descDead']
		else:
			return self.descriptions['descAlive']
	
	
	def take(self):
		if self.properties['bodyHidden']
			return self.descriptions['takeHidden']
		if eng.inInventory(self):
			return self.descriptions['alreadyTakenButler']
		else:
			if self.properties['dead']:
				eng.addToInventory(self) # adds to inventory and removes from current room 
				return self.descriptions['takeButlerDead']
			else:
				return self.descriptions['takeButlerAlive']
	
	
	def drop(self):
		if eng.inInventory(self) == False:
			return self.descriptions['dropNoHold']
		else:
			here = eng.getCurrentRoom()
			if here.name == 'Guest Bedroom':
				score = eng.getScore()
				eng.setScore(score + 20)
				eng.removeFromInventory(self)
				eng.dropItem(self)
				self.properties['bodyHidden'] = True
				return self.descriptions['dropGuest']
			elif here.name == 'Office':
				score = eng.getScore()
				eng.setScore(score + 40)
				eng.removeFromInventory(self)
				eng.dropItem(self)
				self.properties['bodyHidden'] = True
				return self.descriptions['dropOffice']
			elif here.name == 'Second Bedroom':
				return self.descriptions['dropSecond']
			elif here.name == 'Master Bedroom':
				score = eng.getScore()
				eng.setScore(score + 30)
				eng.removeFromInventory(self)
				eng.dropItem(self)
				self.properties['bodyHidden'] = True
				return self.descriptions['dropMaster']
			elif here.name == 'Master Bathroom':
				score = eng.getScore()
				eng.setScore(score + 10)
				eng.removeFromInventory(self)
				eng.dropItem(self)
				self.properties['bodyHidden'] = True
				return self.descriptions['dropBathroom']
			elif here.name == 'Hallway':
				eng.removeFromInventory(self)
				eng.dropItem(self)
				return self.descriptions['dropHallway']
			else:
				# default behavior; this should never happen normally
				eng.removeFromInventory(self)
				eng.dropItem(self)
				return self.descriptions['dropButler']


	def touch(self):
		if self.properties['dead']:
			return self.descriptions['touchButlerDead']
		else:
			return self.descriptions['touchButlerAlive']


	def eat(self):
		return self.descriptions['eatButler']


	def hit(self):
		return self.descriptions['hitButler']


	def talk(self):
		return self.descriptions['talkButler']


	def give(self):
		return self.descriptions['talkButler']


	def kill(self, weapon):
		if self.properties['withMaid']:
			return self.descriptions['killButlerWithMaid']
		if self.properties['dead']:
			return self.descriptions['killDead']
		else:
			if weapon is None:
				return self.descriptions['killButlerUnarmed']
			elif weapon is letterOpener:
				if letterOpener.properties['sharp'] == True:
					self.properties['dead'] = True
					return self.descriptions['killButlerLOSuccess']
				else:
					return self.descriptions['killButlerLOFail']
			else:
				return self.descriptions['killFail']


butler = Butler()
eng.setupItem(butler)
