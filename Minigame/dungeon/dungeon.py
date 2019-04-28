import eng

class dungeon:
    name = "dungeon"
    items = ["torch", "hole", "silver key", "dungeon walls"]
    doors = {"north": "wooden door", "east": "bridge"}
    visible = True

    longDescription = "You're in a dark dungeon and need to find a way out. It's a large room, awful smelling room. There's a lit torch on the north wall illuminating a wooden door"
    shortDescription = "The room you started in"
    lightDescription = "With torch in hand, you explore the room. There's a narrow bridge on the east side and a hole in the ground"

    def enterRoom(self):
        if self.visited:
            return self.shortDescription
        else:
            return self.longDescription

    def look(self):
        torch = eng.getItemByName("torch")
        if eng.inInventory(torch):
            hole = eng.getItemByName("hole")
            bridge = eng.getItemByName("bridge")
            hole.visible = True
            bridge.visible = True
            return self.lightDescription
        else:
            return self.longDescription

dungeon = dungeon()
eng.setupRoom(dungeon)
print(eng.goToRoom(dungeon))