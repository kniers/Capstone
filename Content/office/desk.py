import eng

class Desk:
	name = 'desk'
	#type = 'Item'
	visible = True 
	aliases = []
	descriptions = {'desc': "It's a perfectly adequate desk. It does its job, but it's nothing to write home about. All the drawers are locked. ",
					'hasPenAndOpener': "There's a fountain pen and a letter opener sitting on top of it.",
					'hasPen': "There's a fountain pen sitting on top of it.",
					'hasOpener': "There's a letter opener sitting on top of it.",
					'takeDesk': "It's too heavy. Besides, it wouldn't even fit in your pocket.",
					'touchDesk': "You touch the desk. It doesn't touch you back, except in the Newtonian sense.",
					'eatDesk': "That won't fit in your mouth. Besides, that many calories wouldn't help your figure at all.",
					'useDesk': "This would be a perfect place to do your taxes, but darn it, you didn't bring them.",
					'openDesk': "It's locked. Busting it open would probably attract too much attention."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		currRoom = eng.getCurrentRoom()
		fountainPen = eng.getItemByName('fountain pen')
		if fountainPen is not None:
			fountainPen.visible = True
		letterOpener = eng.getItemByName('letter opener')
		if letterOpener is not None:
			letterOpener.visible = True
		description = self.descriptions['desc']
		if 'fountain pen' in currRoom.items and 'letter opener' in currRoom.items:
			description += self.descriptions['hasPenAndOpener']
		elif 'fountain pen' in currRoom.items:
			description += self.descriptions['hasPen']
		elif 'letter opener' in currRoom.items:
			description += self.descriptions['hasOpener']
		return description
	
	
	def take(self):
		return self.descriptions['takeDesk']


	def touch(self):
		return self.descriptions['touchDesk']


	def open(self):
		return self.descriptions['openDesk']


	def eat(self):
		return self.descriptions['eatDesk']


	def use(self):
		return self.descriptions['useDesk']


desk = Desk()
eng.setupItem(desk)