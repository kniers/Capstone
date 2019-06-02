import eng

class Bible:
	name = 'Bible'
	#type = 'Item'
	visible = False
	aliases = ['King James Bible', 'the good news', 'bible']
	descriptions = {'desc': "A beautiful leather bound bible. On the front cover is a gold cross and seven enlaid diamonds. Must be priceless.",
					'read': "You randomly open the Bible and read. Exodus 20:15 Thou shalt not steal. Okay now you have a guilt trip.",
					'readMore': "Thou shalt not bear false witness against thy neighbour. 'Last thing I want are witnesses', you think.",
					'alreadyHave': "You already have the Good Book. Maybe we should drop it.",
					'takeBible': "Man this thing is heavy. Better be worth the effort.",
					'droppedBible' : "You drop the Bible. 'That is a load off', you think.",
					'warning': "There are people in the room. You can't just take the bible and run! Pretend to care at least until no one is looking.", 
					'dontHave': "You can't drop something you don't have.",
					'huh': "I don't see a bible. ",
					'eatBible': "Do you want to choke to death or God smite you? Take your pick. "}
	properties = {'have': False, 'read': False}

	def look(self):
		if self.visible == True:
			return self.descriptions['desc']
		else:
			return self.descriptions['huh']

	def eat(self):
		return self.descriptions['eatBible']
	

	def take(self):
		if self.properties['read'] == False:
			return self.descriptions['warning']
		if self.properties['read'] == True:
			self.properties['have'] = True 
			eng.addToInventory(self) # adds to inventory and removes from current room 
			#increase score
			score = eng.getScore()
			eng.setScore(score + 30)
			return self.descriptions['takeBible']
		else:
			return self.descriptions['alreadyHave']
		
		
	# drop the Bible, if player is has it 
	def drop(self):
		if self.properties['have'] == False:
			return self.descriptions['dontHave']
		else:
			self.properties['have'] = False
			eng.removeFromInventory(self)
			eng.dropItem(self)
			#reduce score		
			score = eng.getScore()
			eng.setScore(score - 30)
			return self.descriptions['droppedBible']

	def read(self):
		if self.properties['read'] == False:
			self.properties['read'] = True
			return self.descriptions['read']
		else:
			return self.descriptions['readMore']
		
bible = Bible()
eng.setupItem(bible)
