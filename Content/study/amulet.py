import eng

class Amulet:
    name = 'egyptian amulet'
    aliases = ['amulet']

    def look(self):
        return "It's a golden amulet from ancient Egypt. Looks authentic. You have a bad feeling about it..."

    def take(self):
        if eng.inInventory(self):
            return "You already have it"
        else:
            eng.addToInventory(self)
            eng.setScore(eng.getScore() - 5)
            return "You put the amulet in your pocket without drawing too much attention to yourself. A chill goes down your spine. You should not have done that."

    def give(self, recipient):
        if eng.inInventory(self):
            return "You try to give away the amulet, but an unseen force prevents you from taking it out of your pocket."
        else:
            return "You don't have it. If I were you, I wouldn't even pick it up"

    def drop(self):
        if eng.inInventory(self):
            return "An unseen force prevents you from taking out of your pocket. You're cursed."
        else:
            return "You don't have it. If I were you, I wouldn't even pick it up"

    def eat(self):
        if eng.inInventory(self):
            return "You're only going to make things worse."
        else:
            return "You don't have it. If I were you, I wouldn't even pick it up"

    def hit(self):
        if eng.inInventory(self):
            eng.removeFromInventory(self)
            eng.setScore(eng.getScore() + 5)
            return "You manage to break the amulet and free yourself from the curse"
        else:
            return "You don't have it. If I were you, I wouldn't even pick it up"

eng.setupItem(Amulet())