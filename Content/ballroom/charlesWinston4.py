import eng

class CharlesWinston4:
	name = 'CharlesWinston4'
	#type = 'Item'
	visible = True 
	aliases = ['Charles', 'Winston', 'Charles Winston', 'Charles Winston IV', 'Master Winston', 'Sir Charles', 'Mr. Winston', 'ceo', 'CEO']
	descriptions = {'desc': "The CEO is male about 6'2 , looks about mid-fifies, graying hair on the sides, standing in the midst of three other people. He looks very important in the world of old money. It might be best to avoid him or raise suspicion.",
					'intro': "Hello, nice to meet you I am Charles Winston IV. I don't recognize you.",
					'converse':"YOU: I am a friend of, um um, your butler. CHARLES: My butler would never invite a friend to a Winston party. He knows his position.",
					'shock':"Get your hands off me.",
					'suspiciousTalk': "I don't know who you are, but you don't belong here. Wallace escort this man to the door.",
					'sharks': "Yes, I still have those leopard sharks in the basement. I can show you after the party. It will be about time to feed them anyways by then. You know it all started when Uncle Nathaniel brought their descendants back from his adventures. " }
	properties = {'suspicious':False, 'conversation':False}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']

	def talk(self):
		if self.properties['suspicious']:
			return self.descriptions['suspiciousTalk']
		elif self.properties['conversation']:
			self.properties['suspicious'] = True
			return self.descriptions['converse']	
		else:
			self.properties['conversation'] = True
			return self.descriptions['intro']

	def touch(self):
		if self.properties['suspicious']:
			return self.descriptions['suspiciousTalk']
		else:
			self.properties['suspicious'] = True
			return self.descriptions['shock']

	def listen(self):
		return self.descriptions['sharks']

charleswin = CharlesWinston4()
eng.setupItem(charleswin)
