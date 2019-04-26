class masterBathDoor:
	def __init__(self, name, aliases, description, properties, roomConnections):
		self.name = name 
		self.type = "Door"
		self.roomConnections = roomConnections
		self.description = description	
		self.aliases = aliases 
		self.properties = properties
		if "locked" not in self.properties:
			self.properties["locked"] = False

	def setViewed(self):
		self.viewed = True
	
	def getViewed(self): # Can be used to check if room description should be changed
		return self.viewed 	

	def isAlias(self, alias):
		if alias in self.aliases:
			return True
		else:
			return False 
	
	def playerCanPassThrough(self):
		if self.properties["locked"] == False:
			return True
		else:
			return False

	def look(self):
		return self.description

	# get connection from the perspective of the room the player is currently in
	def getConnection(self, direction):
		if direction in self.roomConnections:
			return self.roomConnections[direction]
		else:
			return "No room in that direction"



#TESTING
'''
name = "Master Bathroom Door"
roomConnections = {"north": "Master Bathroom", "South": "Master Bedroom"}
description = "The door from the master bedroom to the master bathroom"
properties = {"locked": True}

door = masterBathDoor(name, [], description, properties, roomConnections)

print(door.look())
print(door.playerCanPassThrough())
'''

