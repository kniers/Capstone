import eng

# a global item to reference the character's person
class character:
    name = "self"
    aliases = ["myself", "yourself"]
    properties = {'placesOpened': 0}
    globalAccess = True

    def look(self):
        return "You look good. The trapped in a dungeon look suits you"

    def kill(self):
        return "Really? The game is that hard that you resort to suicide?"

    def touch(self):
        return "Now is not the time for that"


eng.setupItem(character())