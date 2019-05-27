import eng

# The martini is handed to you by a server when you enter the foyer. It isn't needed for anything, but holding blocks the billiards quest
class Martini:
    name = 'martini'
    aliases = ['dry martini', 'cocktail']

    def look(self):
        return "It's a dry martini that was handed to you by a server. You took it just to blend in with the party, but now you notice that not everyone has a drink."

    def eat(self):
        return "You take a small sip. Better not have too much. Need to keep your wits about you."

    def drop(self):
        if eng.inInventory(self):
            eng.dropItem(self)
            return "You casually set the martini down and walk away."
        else:
            return "You aren't holding it."

    def take(self):
        if eng.inInventory(self):
            return "You're already holding it."
        else:
            eng.addToInventory(self)
            return "You pick your martini up."

    def talk(self):
        return "It's just a drink. Why don't you try talking to people instead?"

    def hit(self):
        eng.removeFromInventory(self)
        return "You wind up and punch the martini glass with all your might. It shatters on the floor. If you didn't want it you could have just set it down. What's wrong with you?\n\nA server quickly sweeps up the glass and leaves."

    def give(self):
        return "No one wants it"

eng.setupItem(Martini())