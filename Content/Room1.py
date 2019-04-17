# This file just for testing engine functionality

import eng

class ExampleItem:
    itemID = "exampleitem"
    description = "A very interesting example"

    def look(self):
        print("I'mma lookin at it")
        #print will need to be replaced with an API that displays text on our UI

    def cook(self, other):
        print("I'm cooking " + other.description)

eng.setupItem(ExampleItem())

#newItem = eng.getItemByID("exampleitem")
#print("Description: " + newItem.description)
ex2 = ExampleItem()
ex2.description = "other example"
ex2.itemID = "ex2"
eng.setupItem(ex2)