import eng

class silverKey:
    name = "silver key"
    aliases = ["key"]
    visible = False

    def look(self):
        return "A polished silver key"

    def take(self):
        if eng.inInventory(self):
            return "You already have it"
        else:
            eng.addToInventory(self)
            dungeon = eng.getRoomByName("dungeon")
            dungeon.items.remove(self.name)
            hole = eng.getItemByName("hole")
            hole.properties["hasKey"] = False
            return "You picked up the key. Maybe this is your way out"

    def use(self, ind=None):
        if not eng.inInventory(self):
            return "You don't have it"
        if ind == None:
            return "Use it on what?"
        door = eng.getItemByName("wooden door")
        chest = eng.getItemByName("chest")
        if ind == door:
            return "You try the silver key from the hole, but it doesn't fit"
        elif ind == chest:
            return chest.open(self)
        else:
            return "Thad didn't work"

eng.setupItem(silverKey())
