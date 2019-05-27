import eng

# This should probably be expanded into something you can steal
class Artifacts:
    name = 'artifacts'

    def look(self):
        return "The walls of the study are lined with all sorts of artifacts from around the world."

eng.setupItem(Artifacts())