import eng

class BilliardLights:
    name = 'billiard lights'
    aliases = ['billiards lights', 'lights', 'pool lights']
    properties = {'broken': False}

    def look(self):
        description = "An ornate set of lights hang just above to billiards table. It's still fairly dark in here. Without the lights it would be impossible to even tell solids from stripes. "
        if self.properties['broken']:
            description += 'The bulbs are broken now, leaving shards across the table.'
        return description

    def take(self):
        room = eng.getRoomByName('Billiard Room')
        if 'billiard players' in room.items:
            return "You go for the lights, but the pool players stop you.\n\"Hey! Can't you see we're in the middle of a game?\""
        else:
            if self.properties['broken']:
                return "You already shattered them. What's the point?"
            else:
                return "No luck, the lights are firmly affixed to the ceiling"

    def hit(self):
        room = eng.getRoomByName('Billiard Room')
        if 'billiard players' in room.items:
            return "You go for the lights, but the pool players stop you.\n\"Hey! Can't you see we're in the middle of a game?\""
        else:
            if self.properties['broken']:
                return "The lights are already broken, thanks to you."
            else:
                return "You smash the ligths above the pool table and they shatter onto the billiard table. Someone has to pay for that you know. "

    def touch(self):
        room = eng.getRoomByName('Billiard Room')
        if 'billiard players' in room.items:
            return "You go for the lights, but the pool players stop you.\n\"Hey! Can't you see we're in the middle of a game?\""
        else:
            if self.properties['broken']:
                return "You pick up pieces of the broken glass and reflect upon all the lives you've destroyed in this line of work. After a moment you snap out of it. Time to get back to stealing!"
            return "The lights are still warm."

eng.setupItem(BilliardLights())