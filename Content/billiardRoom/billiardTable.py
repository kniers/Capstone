import eng

class BilliardTable:
    name = "billiard table"
    aliases = ['pool table']
    properties = {'open': False, 'hasRuby': False, 'hasPlans': False}

    def look(self):
        description = "It's a well-constructed billiard table with a ball return system built in. The woodwork looks fantastic. Is that mahogany? This is no run-of-the-mill table. It must have been built by a true Craftsman. "
        room = eng.getRoomByName('Billiard Room')
        if not 'billiard players' in room.items and self.properties['open'] == False:
            description += "\n\nUpon further inspection, you see a lever on the bottom. "
            lever = eng.getItemByName('table lever')
            lever.visible = True
        if self.properties['open']:
            if self.properties['hasRuby']:
                description += "\n\nA giant ruby is inside!"
            if self.properties['hasPlans']:
                description += "\n\nSome important looking papers are inside!"
        return description

    def touch(self):
        return "You run your fingers along the edge of the felt. It's high quality and hasn't seen much use. "

    def take(self):
        return "Looks heavy. "

    def eat(self):
        return "Have you heard the expression \"So hungry I could eat a pool table\"? Yeah? Me neither... What are you even trying to do??? Your mom always told you to eat more greens, but I don't think felt counts."

eng.setupItem(BilliardTable())