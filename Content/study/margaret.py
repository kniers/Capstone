import eng

class Margaret:
    name = 'margaret'
    aliases = ['woman', 'lady']
    properties = {'hasBeer': True}

    def look(self):
        description = "There's a woman here checking out the collection of artifacts. "
        if self.properties['hasBeer']:
            description += "While it seems everyone else here is drinking fancy cocktails, this woman is double-fisting two glasses of beer."
        return description

    def talk(self, about):
        if about is None:
            if self.properties['hasBeer']:
                martini = eng.getItemByName('martini')
                if eng.inInventory(martini):
                    return "Margaret:\n\"Hello there. I'm Margaret. It's nice to meet you. Isn't this stuff so cool? They were about to run out of beer so I grabbed two glasses. I would offer you one, but it looks like you already have a martini.\""
                else:
                    return "Margaret:\n\"Hello there. I'm Margaret. It's nice to meet you. Isn't this stuff so cool? They were about to run out of beer so I grabbed two glasses. Take one if you want it.\""
            else:
                return "Margaret:\n\"Wow, it must have taken them years to collect this stuff.\""
        elif about.name == 'artifacts':
            if 'mummy\'s curse' in eng.getCurrentRoom().items:
                return "Margaret:\n\"I recognize this one. It's an amulet from ancient Egypt. It's said that any mortal who possesses it would be cursed. Haha, if you believe such a thing!"
            else:
                return "Margaret:\n\"So many interesting things here.\""
        elif about.name == 'beer':
            if self.properties['hasBeer']:
                martini = eng.getItemByName('martini')
                if eng.inInventory(martini):  
                    return "Margaret:\n\"They were almost out at the bar, so I took the last two. I would offer you one, but it looks like you already have a martini.\""
                else:
                    beer = eng.getItemByName('beer')
                    eng.addToInventory(beer)
                    self.properties['hasBeer'] = False
                    return "Mararet:\n\"Here, take one! I'm happy to share.\""
            else:
                return "Margaret:\n\"That's the last beer that they had. Enjoy!\""
	else:
		return "She pretends not to hear you. Evidentally she doesn't want to talk about that."

    def hit(self):
        return "Didn't your mother ever teach you not to hit a woman?"

    def kill(self):
        return "And what purpose would that serve?"

    def touch(self):
        return "You reach out and touch her sholder.\n\nMargaret:\n\"Uh, did you need something?\""

eng.setupItem(Margaret())