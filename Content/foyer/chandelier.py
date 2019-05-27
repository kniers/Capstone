import eng

class Chandelier:
    name = 'chandelier'
    aliases = ['dazzling chandelier', 'lights']

    def look(self):
        return "A beautiful and expensive looking chandelier hangs above the foyer. Even with it's massive size, it doesn't give off too much light. In fact, it looks like the lights are dimmed down in most of the mansion. Perfect"

    def take(self):
        return "That might be a job for another day. How good of a theif do you think you are?"

eng.setupItem(Chandelier())