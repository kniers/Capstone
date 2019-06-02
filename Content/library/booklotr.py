class BookLOTR:
	name = 'The Hobbit'
	#type = 'Item'
	visible = True
	aliases = ['Hobbit', 'LOTR']
	descriptions = {'desc': "Hardbound copy of The Hobbit. ",
					'descHaveBook': "You have The Hobbit in your inventory. ",
					'read': "Three Rings for the Elven-kings under the sky, Seven for the Dwarf-lords in their halls of stone, Nine for Mortal Men, doomed to die, One for the Dark Lord on his dark throne, In the Land of Mordor where the Shadows lie... ",
					'readMore': "One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them. In the Land of Mordor where the Shadows lie... ",
					'alreadyHave': "You already have the book. Maybe we should drop it?",
					'takeBook': "Book is in your inventory.",
					'droppedBook' : "You've dropped the book.", 
					'dontHave': "You can't drop something you don't have.",
					'eatBook': "Seems a bit dusty maybe we shouldn't. "}
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
		
lotr = BookLOTR()
eng.setupItem(lotr)
