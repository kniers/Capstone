import eng

class LightSwitch:
    name = 'light switch'
    aliases = ['switch', 'lightswitch', 'lights!']
    properties = {'lightsOff': False}

    def look(self):
        return "A light switch is concealed by the plants."

    def use(self):
        if self.properties['lightsOff']:
            return "Better not turn the lights back on or they might come back to finish the game."
        else: 
            self.properties['lightsOff'] = True
            room = eng.getCurrentRoom()
            room.items.remove('billiard players')
            return "You inconspicuously flip the light switch and the lights above the table turn off.\nWillie:\n\"Hmm, they must have blown a circuit. What do you say, should we call it a draw?\"\n\nJake:\n\"A draw!? You never stood a chance. Whatever. Let's go grab another drink\"\n\nBoth men exit. Time to take a closer look around."

    def hit(self):
        return self.use()

    def touch(self):
        return "You gently caress the light switch behind the plants as your favorite Metallica song plays in your head. \"Hit the lights!\""

eng.setupItem(LightSwitch())