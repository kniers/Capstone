import eng

class dungeonWalls:
    name = "dungeon walls"
    aliases = ["wall", "walls", "dungeon wall"]

    def look(self):
        torch = eng.getItemByName("torch")
        if eng.inInventory(torch):
            return "The walls look like your standard dungeon walls. Nothing special here."
        else:
            return "You can't see very well. Maybe you should grab that torch"

    def touch(self):
        return "You run your hand along the dungeon walls. Why are they so slimy?"

    def go(self):
        return "You run head first into the wall. Are you ok?"

eng.setupItem(dungeonWalls())