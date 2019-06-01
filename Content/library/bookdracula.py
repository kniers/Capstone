class Bookdracula:
	name = 'Dracula'
	#type = 'Item'
	visible = True
	aliases = ['dracula']
	descriptions = {'desc': "Hardbound, brown leather copy of Dracula. ",
					'descHaveBook': "You have Dracula in your inventory. ",
					'read': "No one but a woman can help a man when he is in trouble of the heart... ",
					'readMore': "Ah, it is the fault of our science that it wants to explain all; and if it explain not, then it says there is nothing to explain... ",
					'alreadyHave': "You already have the book. Maybe we should drop it?",
					'takeBook': "Book is in your inventory.",
					'droppedBook' : "You've dropped the book.", 
					'dontHave': "You can't drop something you don't have.",
					'eatBook': "Can't do that. "}
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
		
bookdracula = Bookdracula()
eng.setupItem(bookdracula)