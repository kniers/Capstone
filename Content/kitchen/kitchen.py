import eng 

class Kitchen:
	name = 'Kitchen'
	visited = False
	visible = False
	aliases = []
	descriptions = {'shortDesc': "You're in the kitchen again. It appears you're still invisible to the staff... weird. " \
								 "There's nothing obvious to grab on the kitchen counter. ", 
					'longDesc': "The door leads you into the kitchen, bustling with staff. It's weird to have a guest in the kitchen, " \
								"but strangely, nobody seems to notice. You actually try to catch a server's attention as she walks by " \
								"but she ignores you. Rude!\n" \
								"I guess if the staff is going to treat you as if you're not there, you can get away with whatever you want. " \
								"Matter of fact, they're probably trained to not confront any of the guests, regardless of what the guest does. " \
								"That's perfect for you - you can just take whatever you need.\n" \
								"As you look around you see that there's a fridge towards the back. That's really the only interesting thing in the room. ",
					'cakeAvailable': "I bet there's still cake in the fridge, though. There's plates of it all around the house and I bet " \
									 "these rich people didn't eat it all. ",
					'smokersDesc': "That'd be perfect for the smokers outside. I'm sure the cake will get them in a more generous mood."}
	doors = {'south': 'ballroomKitchenDoor'}
	items = ['fridge', 'cake']
	properties = {'initialized': False}

			
	def _printShortDesc(self): 
		cake = eng.getItemByName('cake')
		if eng.inInventory(cake):
			return self.descriptions['shortDesc']
		else:
			return self.descriptions['shortDesc'] + self.descriptions['cakeAvailable']

			
	def _printLongDesc(self):
		if self.properties['initialized'] == False:
			self.properties['initialized'] = True
		
		desc = self.descriptions['longDesc']
		smokersTask = eng.getItemByName('smokers')
		if smokersTask.properties['taskStarted']:
			desc += self.descriptions['smokersDesc']
			
		return desc #self.descriptions['longDesc']

		
	def enterRoom(self):
		fridge = eng.getItemByName('fridge')
		fridge.visible = True 
		if (self.visited == True):
			return self._printShortDesc()
		else:
			self.visited = True
			return self._printLongDesc()

			
	# Per game requirements, look should reprint long description 
	def look(self):
		return self._printLongDesc()


kitchen = Kitchen()
eng.setupRoom(kitchen) 