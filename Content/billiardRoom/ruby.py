import eng

class Ruby:
    name = 'Ruby'
    aliases = ['giant ruby']
    visible = False

    def look(self):
        return "Wow, just look at this size of this thing! It's giant! This will fetch a pretty penny."

    def take(self):
        if eng.inInventory(self):
            return "You already have it"
        else:
            eng.setScore(eng.getScore() + 100)
            eng.addToInventory(self)
            eng.getItemByName('billiard table').properties['hasRuby'] = False
            return "What a find! You slip it into your pocket. The boss will be happy to see this! Or maybe you'll just keep it to yourself. You don't get paid enough for this anyway."

    def drop(self):
        if eng.inInventory(self):
            eng.setScore(eng.getScore() - 100)
            eng.dropItem(self)
            return "You set the ruby down in a place that you'll remember"
        else:
            return "You don't have it"

    def eat(self):
        if eng.inInventory(self):
            return "Down the hatch! You try swallowing it, but it's too big"
        else:
            return "You don't have it"

    def give(self, recipient):
        if eng.inInventory(self):
            return "Are you crazy? You should keep that for yourself"
        else:
            return "You don't have it"

eng.setupItem(Ruby())