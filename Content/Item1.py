# This file just for testing engine functionality

import eng

class Item1:
    itemID = "item1"
    description = "A very interesting example"

    def look(self):
        print("I'mma lookin at it")
        #print will need to be replaced with an API that displays text on our UI

    def cook(self, other):
        print("I'm cooking " + other.description)

    def use(self):
        eng.loseGame()

eng.setupItem(Item1())