import eng

class Cars:
    name = 'cars'
    aliases = ['luxary cars']

    def look(self):
        return "Several very expesive cars are parked outside. With enough hard work and dedication, maybe you'll be driving one someday. "

    def take(self):
        return "Stealing a car isn't the best idea. The guards at the end of the driveway will notice."

eng.setupItem(Cars())