import eng

# A shortcut for us to reference the current room as an item
# leaving the object blank will return this
class currentRoom:
    name = "room"
    aliases = ["", "room", "around"]
    globalAccess = True

    def look(self):
        room = eng.getCurrentRoom()
        return room.look()

eng.setupItem(currentRoom())