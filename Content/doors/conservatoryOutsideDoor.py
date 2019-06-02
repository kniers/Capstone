import eng

class ConservatoryOutsideDoor:
    name = 'escape'
    visible = False
    aliases = ['outside', 'out window', 'trees', 'tree line']
    roomConnections = {'west': 'Conservatory', 'east': 'outside'}
    
    # Winning the game
    def go(self):
        score = eng.getScore()
        if score >= 300: # Win
            self.visible = False
            outside = eng.getRoomByName('outside')
            eng.goToRoom(outside)
            eng.winGame()
            return "CONGRATULATIONS! You completed your mission. Big Al will be quite pleased. Type \"quit\" to end the game."
        else:
            return "This would make a great escape route, but you still have work to do. You only have " + str(score) + " points. Anything less than 300 would be an embarrassment."
        
    def look(self):
        return "You can easily escape through the window. A quick sprint to the tree line and you would be home free."

eng.setupDoor(ConservatoryOutsideDoor())