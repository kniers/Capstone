class Bookcharles:
	name = 'Charles Winston'
	#type = 'Item'
	visible = True
	aliases = ['Adventures of Charles Wintor II', 'adventuresofcharleswinston2', 'adventures of charles winston II']
	descriptions = {'desc': "Adventures of Charles Winston II: 1919 to 1923. ",
					'descHaveBook': "You have Adventures of Charles Winston II in your inventory. ",
					'read': "July 8, 1920, Somewhere north of Mt. Everest, We have been going in circles for two days. Maybe I chose the wrong guide... ",
					'readMore': "August 12, 1922, The Great Pyramid is absolutely stunning, but the heat is about to kill me... ",
					'alreadyHave': "You already have the book. Maybe we should drop it?",
					'takeBook': "Book is in your inventory.",
					'droppedBook' : "You've dropped the book.", 
					'dontHave': "You can't drop something you don't have.",
					'eatBook': "You can't even get your mouth around it. "}
	properties = {'have': False, 'read': False}

	def look(self):
		if self.properties['have']:
			return self.descriptions['descHaveBook']
		else:
			return self.descriptions['desc']

	def eat(self):
		return self.descriptions['eatBook']
	

	def take(self):
		if self.properties['have'] == True:
			return self.descriptions['alreadyHave']
		else:
			self.properties['have'] = True
			eng.addToInventory(self) # adds to inventory and removes from current room 
			return self.descriptions['takeBook']
		
	# drop the book , if player is has it 
	def drop(self):
		if self.properties['have'] == False:
			return self.descriptions['dontHave']
		else:
			self.properties['have'] = False
			eng.removeFromInventory(self)
			eng.dropItem(self)
			return self.descriptions['droppedBook']

	def read(self):
		if self.properties['read'] == False:
			self.properties['read'] = True
			return self.descriptions['read']
		else:
			return self.descriptions['readMore']
		
adventuresofcharles = Bookcharles()
eng.setupItem(adventuresofcharles)
