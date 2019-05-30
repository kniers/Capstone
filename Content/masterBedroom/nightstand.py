import eng

class Nightstand:
	name = 'nightstand'
	#type = 'Item'
	visible = True 
	aliases = ['dresser', 'drawer']
	descriptions = {'desc': "It's a nightstand with one drawer.",
					'closedDesc': "There's nothing interesting on top of the nightstand but there may be something in the drawer.",
					'keyDesc': "The drawer is empty except for a key hidden in the back corner of the drawer.",
					'noKeyDesc': "The drawer is open, but there's nothing in there. BORING.",
					'alreadyOpenDesc': "You've already opened that drawer."}
	properties = {'opened': False}

			
	# Verb to get description of item  	
	def look(self):
		if self.properties['opened'] == True:
			currRoom = eng.getCurrentRoom()
			if 'bedroom key' in currRoom.items: # means key has not been picked up/moved, so it's in the drawer 
				return self.descriptions['keyDesc']
			else:
				return self.descriptions['noKeyDesc']
		else:
			return self.descriptions['closedDesc']

			
	def open(self):
		if self.properties['opened'] == True:
			return self.descriptions['alreadyOpenDesc']
		else:
			self.properties['opened'] = True
			key = eng.getItemByName('spare key')
			if key is not None:
				key.visible = True				
			return self.look()
		

nightstand = Nightstand()
eng.setupItem(nightstand)