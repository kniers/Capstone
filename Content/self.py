import eng

# a global item to reference the character's person
class character:
    name = "self"
    aliases = ["myself", "yourself"]
    properties = {'placesOpened': 0}
    globalAccess = True

    def look(self):
        suit = eng.getItemByName('suit')
        gown = eng.getItemByName('gown')
        flower = eng.getItemByName('pink flower')
        if eng.inInventory(suit):
            description = "You look like a fine gentleman. "
            if not eng.inInventory(flower):
                description += "You would look even better with a boutonniere. Maybe there's a flower somewhere around here."
            return description
        elif eng.inInventory(gown):
            description = "You look like a fine lady. "
            if not eng.inInventory(flower):
                description += "You would look even better with an accessory. Maybe there's a flower somewhere around here."
            return description
        else:
            return "You check yourself out in a mirror. You look good dressed in all black. You look like you're ready for anything... except a party that is."

    def kill(self):
        return "Really? The game is that hard that you resort to suicide?"

    def touch(self):
        return "Now is not the time for that."

    def hit(self):
        return "Oof"

    def eat(self):
        return "How do you expect that to work?"

    def take(self):
        return "Try taking items, not yourself"

    def use(self):
        return "And do what, exactly?"

    def talk(self):
        return "You:\n\"You can do this. You're strong. You're smart. You're brave. Get in. Steal stuff. Get out. That's all there is to it.\"\n\nAlso you:\n\"This isn't helping, I need to get to work\""

    def listen(self):
        return "In a moment of introspection, you listen to your heart. You know what you're doing is wrong, but a series of poor life decisions has left you with no other choice."

eng.setupItem(character())
