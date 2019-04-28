import eng

class woodenDoor:
    name = "wooden door"
    aliases = ["door", "wood door"]
    roomConnections = {"north": "endRoom", "south": "dungeon"}
    properties = {"locked": True}

    def look(self):
        return "A thick wooden door"

    def open(self, ind):
        if self.properties["locked"] and ind == None:
            return "It's locked. How will you open it?"
        if self.properties["locked"]:
            doorKey = eng.getItemByName("door key")
            silverKey = eng.getItemByName("silver key")
            if ind == doorKey:
                self.properties["locked"] = False
                return "You used to door key to unlock the door"
            elif ind == silverKey:
                return "You try the silver key from the hole, but it doesn't fit"
            else:
                return "That didn't work"
        else:
            return "It's already open"

    def go(self):
        if self.properties["locked"]:
            return "The door is locked"
        else:
            currentRoom = eng.getCurrentRoom()
            endRoom = eng.getRoomByName("endRoom")
            dungeon = eng.getRoomByName("dungeon")
            if currentRoom == dungeon:
                return eng.goToRoom(endRoom)
            else:
                return eng.goToRoom(dungeon)

eng.setupDoor(woodenDoor())