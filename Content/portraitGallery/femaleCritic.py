import eng

class FemaleCritic:
	name = 'female critic'
	#type = 'Item'
	visible = True 
	aliases = ['critic', 'Stoges', 'woman']
	descriptions = {'desc': "The female critic is intently examining the landscape painting. She's unironically wearing a costume that looks like it belongs in the horse race scene of the movie My Fair Lady.",
					'takeMC': "She's invested in the art. She doesn't want to go anywhere.",
					'touchMC': "That action has several possible results, all of them bad.",
					'talkPortraits': "You ask about the portraits. She ignores you.",
					'talkLandscape': "You ask about the landscape. 'This piece requires more examination before my verdict.' she says. 'How long have you been looking at it?' you ask. She responds 'Oh, about an hour now.'",
					'talkStillLife': "You ask about the still life. 'Ah, what a beautiful piece. Most of this stuff is trash, but that one has soul.'",
					'talkRodin': "You ask about the Rodin statue. 'Oh, don't talk to me about Rodin. The man is a talentless hack.'",
					'talkDefault': "The critic makes an exasperated grunt. She doesn't want to be bothered about that.",
					'talkMaleCritic': "You ask about the male critic. She responds 'Bennings is quite smart, but he always wears the most wretched suits.'",
					'talkNoneWithoutFlowerSuit': "The critic glances at you as you walk up. 'Oh, you look simply ghastly. That tie is an affront to humanity. If you looked any worse, I think I'd throw up!",
					'talkNoneWithoutFlowerGown': "The critic glances at you as you walk up. 'Oh, you look simply ghastly. The colors on that dress clash like the 30 Years War. If you looked any worse, I think I'd throw up!'",
					'talkNoneWithFlower': "The critic glances at you as you walk up. Her eyes flit to the flower you're wearing. The color drains out of her face, and she runs out of the room."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		return self.descriptions['takeMC']


	def touch(self):
		return self.descriptions['touchMC']


	def talk(self, aboutMe):
		if aboutMe is None:
			gown = eng.getItemByName("gown")
			suit = eng.getItemByName("suit")
			flower = eng.getItemByName("pink flower")
			if flower.properties['wearing']:
				currRoom = eng.getCurrentRoom()
				currRoom.items.remove('female critic')
				return self.descriptions['talkNoneWithFlower']
			else:
				if suit.properties['wearing']:
					return self.descriptions['talkNoneWithoutFlowerSuit']
				elif gown.properties['wearing']:
					return self.descriptions['talkNoneWithoutFlowerGown']
		elif aboutMe is portraits:
			return self.descriptions['talkPortraits']
		elif aboutMe is landscape:
			return self.descriptions['talkLandscape']
		elif aboutMe is stillLife:
			return self.descriptions['talkStillLife']
		elif aboutMe is rodinStatue:
			return self.descriptions['talkMcGuffin']
		else:
			return self.descriptions['talkDefault']
			

femaleCritic = FemaleCritic()
eng.setupItem(femaleCritic)
