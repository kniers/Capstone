import eng

# Outside the conservatory. Get here only when you win the game
class Outside:
    name = 'outside'
    visible = False
    doors = {'west': 'escape'}

    def enterRoom(self):
        
        return "" # never shown

    def look(self):
        return "CONGRATULATIONS! You completed your mission. Big Al will be quite pleased. Type \"quit\" to end the game"

eng.setupRoom(Outside())