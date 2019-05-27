import eng

class Craftsman:
    name = 'craftsman'
    aliases = ['man', 'hank']
    properties = {'hasBeer': False}

    def look(self):
        return "This guy is just sitting by himself staring out the window. He does know there's a party going on, right?"

    def hit(self):
        return "Attacking this man doesn't seem worthwhile. "

    def kill(self):
        return self.hit()

    def talk(self, about):
        if about is None:
            if not self.properties['hasBeer']:
                return "You greet the man and he turns to you to reply.\n\nHank:\n\"Hey there. Name's Hank. You don't look like you belong here... Haha, don't worry bout it though. I don't feel like I belong here either. Know where I can get a beer? I hate the taste of these fancy drinks.\""
            else:
                return "Hank:\n\"Thanks for the beer! I don't know anyone else here. I was just invited because I built some stuff for the owners. I'm a Craftsman, ya see.\""
        else:
            if about.name == 'billiardTableTopic':
                lever = eng.getItemByName('table lever')
                lever.visible = True
                return "Hank:\n\"Yeah, I built that pool table in the next room! Let me guess, cue ball got stuck? Here's the secret to getting it open. There's a lever on the bottom of the table and ya gotta whack it. Not just a normal hit, ya really gotta WHACK it. Hear what I'm sayin?\""
            elif about.name == 'mahogany table':
                return "Hank:\n\"I built this table about a year back. They liked it so much they asked me to built a new pool table for them. Just finished it up last week.\""
            elif about.name == 'highball glass':
                return "Hank:\n\"Some server handed me that drink when I walked in the he just kinda disappeared. I didn't want it so I just dropped it\""
            else:
                return "Hank:\n\"I don't know anything about that.\""

eng.setupItem(Craftsman())
