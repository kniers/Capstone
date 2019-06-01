import eng

class Closet:
	name = 'closet'
	#type = 'Item'
	visible = True 
	aliases = ['wardrobe']
	descriptions = {'closedDesc': "It's a closet... Not much more to say about it. Open it if you'd like. ",
					'openDesc': "You open the closet. It's a pretty standard one. ",
					'suitDesc': "Theres a suit hanging in there. ",
					'gownDesc': "There's a gown hanging in there. That's about it. ",
					'bothDesc': "There's a snazzy suit in there, or a gown if that's more your style. ",
					'neitherDesc': "There's nothing in the closet. BORING. ",
					'alreadyOpenDesc': "The closet is already open. You're really trying to open it twice? What does that even mean? "}
	properties = {'opened': False}
	

	def look(self):
		if self.properties['opened'] == True:
			desc = self.descriptions['openDesc']
			# get current room to check if items are in room, adding appropriate descriptions 
			currRoom = eng.getCurrentRoom()
			if 'suit' in currRoom.items and 'gown' in currRoom.items:
				return desc + self.descriptions['bothDesc']
			elif 'suit' in currRoom.items:
				return desc + self.descriptions['suitDesc']
			elif 'gown' in currRoom.items:
				return desc + self.descriptions['gownDesc']
			else:
				return desc + self.descriptions['neitherDesc']
		else:
			return self.descriptions['closedDesc']
	

	def open(self):
		if self.properties['opened'] == True:
			return self.descriptions['alreadyOpenDesc']
		else:
			self.properties['opened'] = True
			currRoom = eng.getCurrentRoom()
			suit = eng.getItemByName('suit')
			if suit is not None:
				suit.visible = True
			gown = eng.getItemByName('gown')
			if gown is not None:
				gown.visible = True				
			return self.look()
		

closet = Closet()
eng.setupItem(closet)
