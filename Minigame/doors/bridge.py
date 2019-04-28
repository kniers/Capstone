import eng

class bridge:
    name = "bridge"
    roomConnections = {"east": "plateau", "west": "dungeon"}
    visible = False

    def look(self):
        return "A narrow bridge. It looks safe enough to cross"

    def go(self):
        plateau = eng.getRoomByName("plateau")
        dungeon = eng.getRoomByName("dungeon")
        currentRoom = eng.getCurrentRoom()
        if currentRoom == plateau:
            return eng.goToRoom(dungeon)
        else:
            return eng.goToRoom(plateau)

eng.setupDoor(bridge())