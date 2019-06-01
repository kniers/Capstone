import eng

# help the player understand they have to specify which one
class Drawers:
    name = 'drawers'
    aliases = ['drawer']
    description = "Which one? There's a top drawer and a bottom drawer"

    def look(self):
        return self.description

    def open(self):
        return self.description

    def take(self):
        return self.description
        
    def eat(self):
        return self.description
        
    def touch(self):
        return self.description

eng.setupItem(Drawers())