import eng

class Booknathaniel:
	name = 'Nathaniel Winston'
	#type = 'Item'
	visible = True
	aliases = ['adventuresofnathanielwinston', 'Adventures of Nathaniel Winston']
	descriptions = {'desc': "Adventures of Nathaniel Winston - 1905 to 1911. It's an old black leather bound book. ",
					'descHaveBook': "There is a gap where the book was. You see a silver button at the back of the bookself",
					'read': "You randomly open the book: July 12, 1907 - 300 miles off the coast of Sumatra. I caught a exceptionally large tiger shark...",
					'readMore': "You turn to the last page: December 25, 1911 - I finally found it! The Eye of Ashoka! It is the most stunning thing I have ever seen.",
					'alreadyHave': "You already have the book. Maybe we should drop it?",
					'takeBook': "Book is in your inventory. You see a silver button behind the book.",
					'droppedBook' : "You've dropped the book.", 
					'dontHave': "You can't drop something you don't have.",
					'eatBook': "Looks delicious...But, do you want to choke to death!?"}
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
			currRoom = eng.getCurrentRoom()
			button = eng.getItemByName('button')
			if button is not None:
				button.visible = True
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
		
booknathaniel = Booknathaniel()
eng.setupItem(booknathaniel)
