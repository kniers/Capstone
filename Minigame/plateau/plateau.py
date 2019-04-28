import eng

class plateau:
    name = "plateau"
    items = ["chest", "door key"]
    doors = {"west": "bridge"}

    longDescription = "You made your way across the bridge to a small plateau with no exits but the way you came. The only thing here is a chest. This isn't the way out. You better go back west across the bridge"
    shortDescriptoin = "You're back on the plateau with the chest. Only way back is the bridge to the west"

    def look(self):
        return self.longDescription

    def enterRoom(self):
        if self.visited:
            return self.shortDescriptoin
        else:
            return self.longDescription

eng.setupRoom(plateau())