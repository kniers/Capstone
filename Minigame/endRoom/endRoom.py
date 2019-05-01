import eng

class endRoom:
    name = "endRoom"
    #this room doesn't have any doors so you can't get out
    
    def look(self):
        return "This is the end"

    def enterRoom(self):
        return "You're out! Congratulations"

eng.setupRoom(endRoom())
