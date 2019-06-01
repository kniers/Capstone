import eng

class Vanity:
	name = 'vanity'
	visible = True 
	aliases = ['drawer']
	descriptions = {'desc': "It's a vanity, a small table for preparing one's self in the morning. ",
					'drawerOpen': "There's an open drawer. ",
					'drawerClosed': "There's a drawer that you can open.",
					'alreadyOpen': "The drawer is already open. ",
					'touchVanity': "You touch the vanity. Nothing happens.",
					'openVanity': "You open the drawer to the vanity. ",
					'stropAndToothpaste': "Inside, there's a strop, a thing of toothpaste, and a bunch of useless crap. ",
					'onlyStrop': "Inside, there's a strop and a bunch of useless crap. ",
					'onlyToothpaste': "Inside, there's some toothpaste and a bunch of other useless crap. ",
					'noItems': "There's just a bunch of useless crap inside - nothing valuable. "}
	properties = {'drawerOpen': False}
	
	
	def look(self):
		self.visible = True
		if self.properties['drawerOpen']:
			return self.descriptions['desc'] + self.descriptions['drawerOpen'] + self._printContents()
		else:
			return self.descriptions['desc'] + self.descriptions['drawerClosed']


	def touch(self):
		return self.descriptions['touchSI']


	def open(self):
		currRoom = eng.getCurrentRoom()
		if self.properties['drawerOpen']:
			return self.descriptions['alreadyOpen'] + self._printContents()
		self.properties['drawerOpen'] = True 
		strop = eng.getItemByName('strop')
		if strop is not None:
			strop.visible = True
		toothpaste = eng.getItemByName('toothpaste')
		if toothpaste is not None:
			toothpaste.visible = True
		
		return self.descriptions['openVanity'] + self._printContents()

			
	def _printContents(self):
		currRoom = eng.getCurrentRoom()
		if 'strop' in currRoom.items and 'toothpaste' in currRoom.items:
			return self.descriptions['stropAndToothpaste']
		elif 'strop' in currRoom.items:
			return self.descriptions['onlyStrop']
		elif 'toothpaste' in currRoom.items:
			return self.descriptions['onlyToothpaste']
		else:
			return self.descriptions['noItems']
			

vanity = Vanity()
eng.setupItem(vanity)