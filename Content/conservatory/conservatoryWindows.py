import eng

class ConservatoryWindows:
    name = 'conservatory windows'
    aliases = ['windows', 'window']
    properties = {'opened': False}

    def look(self):
        return "Lovely floor-to-ceiling windows line the conservatory. It's dark outside so there isn't much to see. "

    def open(self):
        if self.properties['opened']:
            return "The windows are already open."
        else:
            self.properties['opened'] = True
            return "You open a couple windows and a warm breeze rolls in. "

    def close(self):
        if self.properties['opened']:
            self.properties['opened'] = False
            return "You close the windows. They were letting in too much smoke anyway."
        else:
            return "The windows are already closed."

    def hit(self):
        return ""

eng.setupItem(ConservatoryWindows())
