import eng

class MahoganyTable:
    name = 'mahogany table'
    aliases = ['table', 'wood table', 'wooden table']

    def look(self):
        return "This is a fine mahogany table. You've seen woodwork like this somewhere else tonight... A highball glass sits on the table"

eng.setupItem(MahoganyTable())