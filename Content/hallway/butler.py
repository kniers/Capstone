import eng

class Butler:
	name = 'butler'
	#type = 'Item'
	visible = True 
	aliases = []
	descriptions = {'descAlive': "The butler is standing at the top of the stairway, observing the party below. You can't sneak past him without arousing his suspicion. You could kill him if you had a weapon, but Big Al would prefer this mission be done quietly.",
					'descDead': "The butler's body is still right where you left it.",
					'takeButlerAlive': "You mean, like to dinner? I don't think he'd be interested.",
					'takeButlerDead': "You pick up the butler's body. Now to get it out of sight.",
					'touchButlerAlive': "That would attract his attention, something you don't want at the moment.",
					'touchButlerDead': "You poke the body. Yep, he's definitely dead.",
					'eatButler': "Ew, no.",
					'killButlerUnarmed': "You jump on the butler and begin pummeling him with your fists. He's very spry for his age, and manages to twist out of your grip. As you spar, he calls for help. You hear the sound of footsteps on the stairs. They have guns...\n\nYou snap out of the daydream. That won't work.",
					'killButlerLOFail': "The letter opener isn't very sharp. The butler would call for help before you got him.",
					'killButlerLOSuccess': "You cover the butler's mouth with one hand and stab his neck with the other. Success. You probably should hide the body so they can't track the murder back to Big Al.",
					'killFail': "That's probably not the best weapon.",
					'killDead': "Stop! Stop! He's already dead!",
					'alreadyTakenButler': "You've already got the body."}
	properties = {'dead': False}
	
	
	def look(self):
		self.visible = True
		if self.alive:
			return self.descriptions['descDead']
		else:
			return self.desciptions['descAlive']
	
	
	def take(self):
		if eng.inInventory(self):
			return self.descriptions['alreadyTakenButler']
		else:
			if self.dead:
				eng.addToInventory(self) # adds to inventory and removes from current room 
				return self.descriptions['takeButlerDead']
			else:
				return self.descriptions['takeButlerAlive']
		#FIXME: We should prevent the player from carrying the butler downstairs somehow.


	def drop(self, dropPoint):
		#FIXME: Give varying amounts of points depending on how good the player's hiding place is


	def touch(self):
		if self.dead:
			return self.descriptions['touchButlerDead']
		else:
			return self.descriptions['touchButlerAlive']


	def eat(self):
		return self.descriptions['eatButler']


	def kill(self, weapon):
		if self.dead:
			if weapon is None:
				return self.descriptions['killButlerUnarmed']
			elif weapon is letterOpener:
				if letterOpener.sharp:
					self.dead = True
					return self.descriptions['killButlerLOSuccess']
				else
					return self.descriptions['killButlerLOFail']
			else
				return self.descriptions['killFail']
		else:
			return self.desciptions['killDead']
		


butler = Butler()
eng.setupItem(butler)