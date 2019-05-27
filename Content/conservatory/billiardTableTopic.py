import eng

# Putting this in the conservatory so you can talk about it
class BilliardTableTopic:
    name = 'billiardTableTopic'
    aliases = ['billiard table', 'pool table', 'billiards table', 'lever', 'table lever', 'billiard lever']

    def look(self):
        return "You mean the billiard table in the other room? I wonder if this guy knows anything about it."

eng.setupItem(BilliardTableTopic())