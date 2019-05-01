import eng

class doorKey:
    name = "door key"
    aliases = ["key"]
    visible = False

    def look(self):
        return "A door key. Hopefully this is your way out!"
    
    def take(self):
        if eng.inInventory(self):
            return "You already have it"
        else:
            eng.addToInventory(self)
            chest = eng.getItemByName("chest")
            chest.properties["hasKey"] = False
            return "You picked up the door key"

    def use(self, ind):
        if ind == None:
            return "Use it on what?"
        door = eng.getItemByName("wooden door")
        if ind == door:
            return door.open(self)
        else: 
            return "That didn't work"

eng.setupItem(doorKey())