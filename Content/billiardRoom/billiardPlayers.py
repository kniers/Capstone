import eng

# When they leave, visible is set to false
class BilliardPlayers:
    name = 'billiard players'
    aliases = ['players', 'billiards players', 'gentlemen', 'pool players', 'willie', 'jake']
    properties = {'initialized': False}
    descriptions = {'initial': "Willie:\n\"You just got lucky on the break. There's no way you can beat me again. What do you say - double or nothing?\"\n\nJake:\n\"Why can't you admit defeat? You're just embarrasing yourself. I'll beat you again if that's what you want. You can even break this time.\"",
                    'other': "They mumble to themselves as they take turns scuffing up the table. Neither of them are any good."}

    def look(self):
        if self.properties['initialized']:
            return self.descriptions['other']
        else:
            self.properties['initialized'] = True
            return self.descriptions['initial']
    
    def talk(self):
        conversation = self.look()
        return conversation + "\n\nThey're focused on their game and probably don't want to talk."

    def touch(self):
        return "You awkwardly touch one of the players as he lines up a shot. He didn't seem to notice, but there doesn't seem to be anything valuable in his pockets."

    def hit(self):
        return "\"Hey! Can't you see we're in the middle of something? I'm not in the mood for a fight.\""

    def kill(self):
        return self.hit()

eng.setupItem(BilliardPlayers())