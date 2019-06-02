import eng

class TableLever:
    name = 'table lever'
    aliases = ['lever']
    visible = False
    properties = {'used': False}

    def look(self):
        return "A small lever is on the underside of the billiard table. It's probably opens up the ball return system. "

    def take(self):
        room = eng.getCurrentRoom()
        if 'billiard players' in room.items:
            return "You can't get up to it because the players are in the way"
        return "The lever is firmly attached to the table. What do you want with it anyway?"

    def use(self): 
        room = eng.getCurrentRoom()
        if 'billiard players' in room.items:
            return "You can't get up to it because the players are in the way"
        return "You fiddle around with the lever under the billiard table. You try pushing, pulling, and turning, but nothing happens. It doesn't even budge. You don't see a keyhole anywhere. There must be some secret to it..."

    def open(self):
        return self.use()

    def touch(self):
        return self.use()

    # Opens table
    def twist(self):
        if self.properties['used']:
            return "You twist it again, but nothing happened."
        else:
            self.properties['used'] = True
            room = eng.getCurrentRoom()
            if 'billiard players' in room.items:
                return "You can't get up to it because the players are in the way"
            else:
                description = "With a great amount of force, you twist the lever and it opens a panel on the side of the pool table. "
                table = eng.getItemByName('billiard table')
                table.properties['open'] = True
                character = eng.getItemByName('self')
                character.properties['placesOpened'] += 1
                if character.properties['placesOpened'] == 3:
                    room.items.append('secret plans')
                    table.properties['hasPlans'] = True
                    description += "\n\nThere are some papers hidden inside!"
                else:
                    table.properties['hasRuby'] = True
                    ruby = eng.getItemByName('Ruby')
                    ruby.visible = True
                    description += "\n\nA giant ruby is inside!"
                return description

    def hit(self):
        return "You don't want to break the lever off just in case it's of some importance. There must be a secret to it..."
        

eng.setupItem(TableLever())