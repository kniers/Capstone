import eng

class Bookshelf:
	name = 'bookshelf'
	#type = 'Item'
	visible = True 
	aliases = ['bookcase', 'book shelf', 'book case']
	descriptions = {'bookshelfDesc': "There is a long bookshelf that runs the length of the east wall from floor to ceiling. It is filled with numerous books. From here you see Great Expectations, Lord of the Rings, Charles Winston, Nathaniel Winston, and Dracula. ",
					'pushedDesc': "A three foot wide portion of the bookself has been lowered into the floor. You can see at iron door. ",
					'bookremovedDesc': "Where the Adverntues of Nathaniel Winston was you see a silver button along the back of the bookshelf. "}
	properties = {'buttonPushed': False, 'bookRemoved': False}

	def look(self):
		if self.properties['buttonPushed'] == True:
			desc = self.descriptions['pushedDesc']
			currRoom = eng.getCurrentRoom()
		elif self.properties['bookRemoved']:
			return self.descriptions['bookremovedDesc']
			
		else:
			return self.descriptions['bookshelfDesc']	

bookshelf = Bookshelf()
eng.setupItem(bookshelf)
