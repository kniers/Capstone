class Bookgreat:
	name = 'Great Expectations'
	#type = 'Item'
	visible = True
	aliases = ['great expectations', 'GreatExpectations']
	descriptions = {'desc': "Hardbound, green leather copy of Great Expectations. ",
					'descHaveBook': "You have Great Expectations in your inventory. ",
					'read': "Suffering has been stronger than all other teaching, and has taught me to understand what your heart used to be... ",
					'readMore': "Heaven knows we need never be ashamed of our tears, for they are rain upon the blinding dust of earth, overlying our hard hearts... ",
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
		
greatexpectations = Bookgreat()
eng.setupItem(greatexpectations)