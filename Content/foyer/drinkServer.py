import eng

# Server in the foyer hands you a drink when you first enter, then seems to disappear
class DrinkServer:
    name = 'drink server'
    aliases = ['server']
    descriptions = {'talk': "You look around for the server who handed you a martini, but he's nowhere to be found.",
                    'attack': "The martini tasted like garbage, so you decide to take matters into your own hands. Hellbent on revenge, you look for the server to give him a piece of your mind. Alas, he's nowhere to be found."}

    def look(self):
        return self.descriptions['talk']

    def talk(self):
        return self.descriptions['talk']

    def hit(self):
        return self.descriptions['attack']

    def kill(self):
        return self.descriptions['attack']

eng.setupItem(DrinkServer())