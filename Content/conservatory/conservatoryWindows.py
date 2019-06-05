import eng

class ConservatoryWindows:
    name = 'conservatory windows'
    aliases = ['windows', 'window']
    properties = {'opened': False, 'broken': False}

    def look(self):
        return "Lovely floor-to-ceiling windows line the conservatory. It's dark outside so there isn't much to see. The back of the estate is surrounded by woods. "

    def open(self):
        if self.properties['broken']:
            return "You already broke the window. Let's just say you permanently opened it."
        else:
            if self.properties['opened']:
                return "The windows are already open."
            else:
                self.properties['opened'] = True
                escape = eng.getItemByName('escape')
                escape.visible = True
                return "You open a couple windows and a warm breeze rolls in. "

    def close(self):
        if self.properties['broken']:
            return "You already broke the window. There's no putting it back together."
        else:
            if self.properties['opened']:
                self.properties['opened'] = False
                escape = eng.getItemByName('escape')
                escape.visible = False
                return "You close the windows. They were letting in too much fresh air anyway."
            else:
                return "The windows are already closed."

    def hit(self):
        if self.properties['broken']:
            return "You already broke a window. "
        else:
            self.properties['broken'] = True
            escape = eng.getItemByName('escape')
            escape.visible = True
            return "You smash one of the windows. Shards of glass scatter across the floor."

    def go(self):
        if self.properties['broken'] or self.properties['opened']:
            escape = eng.getItemByName('escape')
            return escape.go()
        else:
            return "You can't go though a closed window."

eng.setupItem(ConservatoryWindows())
