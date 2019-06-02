import eng

class GuardShack:
    name = 'guard shack'
    aliases = ['shack', 'guardshack']

    def look(self):
        return "A guard shack is located at the end of the driveway. They're probably checking out everyone who comes and goes."

eng.setupItem(GuardShack())