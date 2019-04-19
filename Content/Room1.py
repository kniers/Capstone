import eng

class Room1:
    roomID = "room1"
    description = "You're in room 1"

    def enter(self):
        print("You entered room 1")
        item = eng.getItemByID("item1")
        eng.addToInventory(item)


eng.setupRoom(Room1())