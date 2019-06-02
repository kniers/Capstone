import eng

class Button:
	name = 'button'
	#type = 'Item'
	visible = False 
	aliases = ['silverbutton', 'silver button']
	descriptions = {'buttonDesc': "It is a silver button just begging to be pushed. ",
					'pushedDesc': "Looks like the button opened a three foot wide portion of the bookshelf. There is an iron hatch behind the case. ",
					'bookshelfCloses': "The three foot portion of the bookshelf rises out of the flooring hiding the iron hatch. ",
					'bookshelfOpens': "A three foot portion of the bookshelf lowers into a compartment in the floor. This reveals an iron hatch in the floor behind the shelving. "}
	properties = {'buttonPushed': False}

	def look(self):
		if self.properties['buttonPushed'] == True:
			return self.descriptions['pushedDesc']
		else:
			return self.descriptions['buttonDesc']	

	def push(self):
		if self.properties['buttonPushed'] == True:
			self.properties['buttonPushed'] = False
			currRoom = eng.getCurrentRoom()
			bookself = eng.getItemByName('bookshelf')
			bookself.properties['buttonPushed'] = False
			secretDoor = eng.getItemByName('librarySecretRoomDoor')
			if secretDoor is not None:
				secretDoor.visible = False
			return self.descriptions['bookselfCloses']
		else:
			self.properties['buttonPushed'] = True
			currRoom = eng.getCurrentRoom()
			bookself = eng.getItemByName('bookshelf')
			bookself.properties['buttonPushed'] = True
			secretDoor = eng.getItemByName('librarySecretRoomDoor')
			if secretDoor is not None:
				secretDoor.visible = True				
			return self.descriptions['bookshelfOpens']	

button = Button()
eng.setupItem(button)
