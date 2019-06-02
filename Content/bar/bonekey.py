import eng

class BoneKey:
	name = 'bone key'
	#type = 'Item'
	visible = False
	aliases = ['bonekey', 'key']
	descriptions = {'desc': "Looks to be a key fashioned from some animal or human bone... ",
					'alreadyHave': "You already have the key. Maybe we should drop it?",
					'takeKey': "You got the bone key. How medieval. ",
					'droppedKey' : "You've dropped the bone key. ", 
					'dontHave': "You can't drop something you don't have.",
					'eatKey': "There is no meat left on the bone. "}
	properties = {'have': False}

	def look(self):
		if self.visible == True:
			return self.descriptions['desc']

	def eat(self):
		if self.visible == True:
			return self.descriptions['eatKey']

	def take(self):
		if self.visible == True:
			if self.properties['have'] == True:
				return self.descriptions['alreadyHave']
			else:
				self.properties['have'] = True 
				currRoom = eng.getCurrentRoom()
				bonekey = eng.getItemByName('bone key')
				if bonekey is not None:
					eng.addToInventory(self)
					return self.descriptions['takeKey']
		
	# drop the bone key, if player is has it 
	def drop(self):
		if self.properties['have'] == False:
			return self.descriptions['dontHave']
		else:
			self.properties['have'] = False
			eng.removeFromInventory(self)
			eng.dropItem(self)
			return self.descriptions['droppedKey']

	def use(self, item):
		if item is None:
			return "Use it on what?"
		if item.name == 'librarySecretRoomDoor':
			return item.open(self)

		
bonekey = BoneKey()
eng.setupItem(bonekey)
