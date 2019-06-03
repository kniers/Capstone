import eng

class Counter:
	name = 'counter'
	#type = 'Item'
	visible = True 
	aliases = ['Counter', 'marble counter']
	descriptions = {'desc': "Bar counter stretches most of the length of the room. The counter top is of fine marble. There are taps with five selections of craft beer. Maybe I should investigate the bar counter.",
					'searched': "Searching under the marble counter top you feel something. Feels like a bone, or maybe a key. Or both!? "}
	properties = {'looked': False}

	def look(self):
		self.properties['looked'] = True
		return self.descriptions['desc']

	#search bar counter to find bone key
	def investigate(self):
		#if self.properties['looked']:
		currRoom = eng.getCurrentRoom()
		bonekey = eng.getItemByName('bone key')
		if bonekey is not None:
			bonekey.visible = True
			return self.descriptions['searched']

barcounter = Counter()
eng.setupItem(barcounter)
