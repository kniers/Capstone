class masterBathDoor:
	def __init__(self, roomConnections, description, properties):
		self.roomConnections = roomConnections.copy()
		self.description = description	
		self.properties = properties.copy()
		if "locked" not in self.properties:
			self.properties["locked"] = False 
	
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
roomConnections = {"north": "Master Bathroom", "South": "Master Bedroom"}
description = "The door from the master bedroom to the master bathroom"
properties = {"locked": True}

door = masterBathDoor(roomConnections, description, properties)

print(door.look())
print(door.playerCanPassThrough())
'''

