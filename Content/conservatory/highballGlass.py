import eng

class HighballGlass:
    name = 'highball glass'
    aliases = ['glass']

    def look(self, other):
        return "A full drink in a highball glass sits on the table. The ice has melted and it doesn't look like it's been touched."

    def take(self, other):
        return "You reach for the glass.\n\nHank:\n\"Oh, that's mine but I guess you can have it. Wasn't gonna drink it anyways. You know if anyone around here has any beer? That would really hit the spot\"\n\n You leave the glass on the table. You don't need to be taking other people's drinks."

    def eat(self, other):
        return self.take(None)

eng.setupItem(HighballGlass())