import eng

class masterBedDoor:
	name = "masterBedDoor"
	
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
		masterBed = eng.getRoomByName("Master Bedroom")
		hall = eng.getRoomByName("Hallway")
		currRoom = eng.getCurrentRoom()
		if currRoom == masterBed:
			return eng.goToRoom(hall)
		else:
			return eng.goToRoom(masterBed)


	def look(self):
		return self.description

	# get connection from the perspective of the room the player is currently in
	def getConnection(self, direction):
		if direction in self.roomConnections:
			return self.roomConnections[direction]
		else:
			return "No room in that direction"



aliases = ["door", "hallway door"]
roomConnections = {"east": "Master Bedroom", "west": "Hallway"}
description = "Upon further inspection... there's nothing special about this door. It looks like any other door you've ever seen."
properties = {"locked": False}

masterBedDoor = masterBedDoor(aliases, description, properties, roomConnections)
eng.setupDoor(masterBedDoor)