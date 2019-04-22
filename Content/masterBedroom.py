# Master Bedroom 

from Room import *

class MasterBedroom(Room):
	shortDesc = "You're back in the bedroom that you started in.\n" \
				"It doesn't look like anyone has been in here since you left,\n" \
				"although it's hard to be sure."
	longDesc = "You find yourself in what appears to be the master bedroom.\n" \
				"Behind you is the window you entered in,\n" \
				"although it probably won't be too useful without your ladder!\n" \
				"There is a closet in front of you and a door to the left.\n" \
				"An open door to the right reveals the master bathroom. Pretty nice if you ask me!\n" \
				"You're pretty stuck here right now. The window isn't really an option\n" \
				"to leave through, so your only option is to somehow be a part of the party.\n" \
				"You're dressed like a burglar, so that's not going to work either.\n" \
				"There's got to be a way to sneak out or a way to change your appearance!\n"
	
	def __init__(self, doorsToAdd, itemsToAdd):
		Room.__init__(self, doorsToAdd, itemsToAdd)

			
doors = {'North': 'Bathroom door', 'South': 'Bedroom door'}
items = ['suit']			
firstRoom = MasterBedroom(doors, items)

print(firstRoom.printDescription())
firstRoom.setVisited()
print(firstRoom.printDescription())

if (firstRoom.doorInRoom("Bathroom door") == True):
	print("\nThere is a bathroom door in the room")
if (firstRoom.doorInRoom("Closet") == False):
	print("\nThere isn't a closet in the room")

if (firstRoom.itemInRoom("suit") == True):
	print("\nThere is a suit in the room")