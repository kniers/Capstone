import eng

class Guards:
    name = 'guards'
    
    def look(self):
        currRoom = eng.getCurrentRoom()
        if 'old lady' in currRoom.items:
            return "Oh no! The guards are coming down the driveway! You better go back inside and find another way out."
        else:
            return "You don't see any guards around, but there's a light on in the guard shack."

    def kill(self):
        return "You're outnumbered. It would never work."

eng.setupItem(Guards())