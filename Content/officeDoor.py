import eng

class officeDoor:
	name = "officeDoor"
	
	def __init__(self, aliases, description, properties, roomConnections):
		self.type = "Door"
		self.visible = True 
		self.roomConnections = roomConnections
		self.description = description	
		self.aliases = aliases 
		self.properties = properties
		if "locked" not in self.properties:
			self.properties["locked"] = False	

	def isAlias(self, alias):
		if alias in self.aliases:
			return True
		else:
			return False 
	
	def go(self):
		office = eng.getRoomByName("Office")
		hall = eng.getRoomByName("Hallway")
		currRoom = eng.getCurrentRoom()
		if currRoom == office:
			return eng.goToRoom(hall)
		else:
			return eng.goToRoom(office)


	def look(self):
		return self.description

	# get connection from the perspective of the room the player is currently in
	def getConnection(self, direction):
		if direction in self.roomConnections:
			return self.roomConnections[direction]
		else:
			return "No room in that direction"



aliases = ["door"]
roomConnections = {"north": "Hallway", "south": "Office"}
description = "Upon further inspection... there's nothing special about this door. It's from the hall to the office."
properties = {"locked": False}

officeDoor = officeDoor(aliases, description, properties, roomConnections)
eng.setupDoor(officeDoor)