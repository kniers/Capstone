import eng

class DecorativePlants:
    name = 'decorative plants'
    aliases = ['artificial plants', 'plant', 'plants', 'potted plants']
    
    def look(self):
        eng.getItemByName('light switch').visible = True
        return "A few artificial potted plants are lined up along the south wall. There's a light switch hidden behind them. "

    def eat(self):
        return "You break off a leaf and eat it. As you swallow, you come to terms with the fact that you just ate a plastic leaf from a clearly artificial plant. If you're that hungry, why don't you see if they have anything in the refrigerator. "

    def take(self):
        eng.getItemByName('light switch').visible = True
        return "You bend over and try to lift one of the potted plants. You can barely get it off the ground. However, you notice a light switch hidden behind it."

eng.setupItem(DecorativePlants())