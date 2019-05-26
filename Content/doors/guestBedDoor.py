import eng

class GuestBedDoor:
	name = 'guestBedDoor'
	visible = True 
	aliases = ['door']
	roomConnections = {'south': 'Hallway', 'north': 'Guest Bedroom'}
	descriptions = {'desc': "Upon further inspection... there's nothing special about this door. It's from the hall to the guest bedroom."}
	properties = {'locked': False}

	
	def go(self):
		bedroom = eng.getRoomByName('Guest Bedroom')
		hall = eng.getRoomByName('Hallway')
		currRoom = eng.getCurrentRoom()
		if currRoom == bedroom:
			return eng.goToRoom(hall)
		else:
			return eng.goToRoom(bedroom)


	def look(self):
		return self.descriptions['desc']


guestBedDoor = GuestBedDoor()
eng.setupDoor(guestBedDoor)