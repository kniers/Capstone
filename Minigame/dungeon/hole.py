import eng

class hole:
    name = "hole"
    aliases = ["ground", "down"]
    properties = {"hasKey": True}
    visible = False

    def look(self):
        if self.properties["hasKey"]:
            key = eng.getItemByName("silver key")
            key.visible = True
            return "A small hole in the ground. Just big enough to get your foot stuck. There a key sitting in it"
        else:
            return "A small hole in the ground"
    
    def go(self):
        return "It's far too small to fit down"

eng.setupItem(hole())