import eng

# This teaches the player about the 'drop' command. There's no way to actually steal it
class Masterpiece:
    name = 'masterpiece'
    aliases = ['painting', 'magnificant painting', 'huge painting', 'abstract painting']

    def look(self):
        if eng.inInventory(self):
            return "This is a huge painting that you're attempting to steal. There's no way to conceal it. You should probably drop it and focus on your mission."
        else:
            return "It's a huge abstract painting. On the surface it's just a bunch of seemingly random colors... but it invokes strong emotions that remind you of your childhood. It must be a masterpiece. Probably worth a lot of money, too."

    def touch(self):
        return "You feel a special connection to this piece of art, but touching it reminds you that it's just simple paint on a canvas."

    def eat(self):
        return "Well, that's one way to get it out of here, but it probably won't taste good"

    def drop(self):
        if eng.inInventory(self):
            eng.dropItem(self)
            eng.setScore(eng.getScore() - 1000000)
            return "There was no way you were going to get that out of here anyway. You prop it against a wall."
        else:
            return "You aren't holding it"
    
    def take(self):
        if eng.inInventory(self):
            return "You already have it"
        else:
            eng.addToInventory(self)
            eng.setScore(eng.getScore() + 1000000)
            return "You take the painting. It's a true masterpiece and must be worth a fortune. Unfortunately, it's way too big to conceal. You should probably drop it before heading into the party."
        
    def hit(self):
        return "That's not a good idea"

    def give(self):
        return "You better not try to give this to anyone since you clearly stole it."

eng.setupItem(Masterpiece())