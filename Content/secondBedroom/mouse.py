import eng

class Mouse:
	name = 'mouse'
	#type = 'Item'
	visible = False 
	aliases = []
	descriptions = {'desc': "The mouse is sitting in the trap, seemingly unharmed. It's twitching it's nose at you.",
					'outOfTrap': "The mouse looks ecstatic to be out of that trap! You hold it tight so it doesn't get away from you.",
					'takeMouse': "You open the trap and grab the mouse.",
					'alreadyTakenMouse': "You already took that.",
					'touchMouse': "You reach your finger towards the mouse, but it cowers from you.",
					'eatMouse': "YUCK! NO!",
					'dropNoHold': "You have to pick him up first.",
					'dropYes': "You release the mouse into the room and hide behind the door. The mouse runs towards the maid and touches her leg. The maid wakes up. She looks around for a moment, sees the mouse, and then starts screaming. Moments later the butler enters the room.\n\nThe butler puts his arm around her and begins whispering some rather sappy things into her ear. They won't notice you, but you'd better slip out before you start to feel nauseated.",
					'dropNo': "You reach for the mouse, but pause. There's a better place to let the little guy go.",
					'dropButlerDead': "You release the mouse into the room. He runs under the bed and disappears. Oh well.",
					'nokill': "--No animals were harmed in the making of this game.--"}
	properties = {}
	
	
	def look(self):
		if eng.inInventory(self):
			return self.descriptions['outOfTrap']
		else:
			return self.descriptions['desc']
	
	
	def take(self):
		if eng.inInventory(self):
			return self.descriptions['alreadyTakenMouse']
		else:
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['takeMouse']


	def touch(self):
		return self.descriptions['touchMouse']


	def eat(self):
		return self.descriptions['eatMouse']


	def drop(self):
		butler = eng.getItemByName("butler")
		if eng.inInventory(self) == False:
			return self.descriptions['dropNoHold']
		elif butler.properties['dead'] == True:
			return self.descriptions['dropButlerDead']
		else:
			currRoom = eng.getCurrentRoom()
			if currRoom.name == "Guest Bedroom":
				hlwy = eng.getRoomByName("Hallway")
				hlwy.items.remove('butler')
				eng.dropItem(butler)
				butler.properties['withMaid'] = True
				currRoom.properties['maidAsleep'] = False
				eng.removeFromInventory(self)
				score = eng.getScore()
				eng.setScore(score + 50)
				return self.descriptions['dropYes']
			else:
				return self.descriptions['dropNo']
			
	def hit(self):
		return self.descriptions['nokill']

	def kill(self):
		return self.descriptions['nokill']

mouse = Mouse()
eng.setupItem(mouse)