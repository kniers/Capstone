import eng

# a global item to reference the character's person
class character:
    name = "self"
    aliases = ["myself", "yourself"]
    globalAccess = True

    def look(self):
        return "You look good. The trapped in a dungeon look suits you"

    def kill(self):
        return "Really? The game is that hard that you resort to suicide?"

    def touch(self):
        return "Nows not the time for that"


eng.setupItem(character())