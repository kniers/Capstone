import eng

class torch:
    name = "torch"
    aliases = ["lit torch"]

    def look(self):
        return "A convenient, but small torch"

    def take(self):
        if eng.inInventory(self):
            return "You already have it"
        else:
            eng.addToInventory(self)
            return "You take the torch off the wall. Your visibility has improved"

    def use(self):
        if eng.inInventory(self):
            room = eng.getCurrentRoom()
            return room.look()
        else:
            return "You can't use it while it's still on the wall"

eng.setupItem(torch())