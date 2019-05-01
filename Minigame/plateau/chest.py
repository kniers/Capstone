import eng

class chest:
    name = "chest"
    properties = {"locked": True, "hasKey": True}

    def look(self):
        if self.properties["locked"]:
            return "A run of the mill dungeon chest. It's closed"
        else:
            if self.properties["hasKey"]:
                return "The chest is open and there's a door key inside"
            else:
                return "The chest is open with nothing else in it"

    def take(self):
        return "You attempt to lift the chest, but it's too heavy"

    def open(self, ind):
        if self.properties["locked"] and ind == None:
            return "It's locked. How will you open it?"
        if self.properties["locked"]:
            silverKey = eng.getItemByName("silver key")
            if ind == silverKey:
                self.properties["locked"] = False
                doorKey = eng.getItemByName("door key")
                doorKey.visible = True
                return "The silver key opened the chest. Looks like another key is inside of it. You recognize the unique shape of a door key"
            else:
                return "That didn't work"
        else:
            return "It's already open"
        

eng.setupItem(chest())