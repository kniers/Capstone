import eng

class Beer:
    name = 'beer'
    aliases = ['bottle']

    def look(self):
        return "A bottle of high quality beer. You haven't seen any others around the party"

    def take(self):
        martini = eng.getItemByName('martini')
        if eng.inInventory(martini):
            return "Margaret:\n\"I would be happy to share one, but they're all out at the bar and it looks like you already have a martini.\""
        else:
            margaret = eng.getItemByName('margaret')
            if margaret.properties['hasBeer']:
                eng.addToInventory(self)
                margaret.properties['hasBeer'] = False
                return "Margaret:\n\"Here you go. Enjoy!\""
            else:
                return "You already have it."    

    def eat(self):
        return "Something tells you that you have a better use for it"

    def give(self, recipient):
        if eng.inInventory(self):
            if recipient is None:
                return "Give it to whom?"
            elif recipient.name == 'craftsman':
                eng.removeFromInventory(self)
                recipient.properties['hasBeer'] = True
                return recipient.talk(None)
            else:
                return "\"Thank you, but I don't want that.\""
        else:
            return "You don't have it, so you can't give it to anyone now can you?"

eng.setupItem(Beer())