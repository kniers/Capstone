import eng

class BoneKey:
	name = 'bone key'
	#type = 'Item'
	visible = False
	aliases = ['bonekey']
	descriptions = {'desc': "Looks to be a key fashioned from some animal or human bone... ",
					'alreadyHave': "You already have the key. Maybe we should drop it?",
					'takeKey': "Bone key is in your inventory. ",
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

		
bonekey = BoneKey()
eng.setupItem(bonekey)
