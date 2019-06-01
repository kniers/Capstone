import eng

class OldLady:
	name = 'old lady'
	#type = 'Item'
	visible = True 
	aliases = ['Mrs. Haut', 'Bethal Haut', 'Bethal']
	descriptions = {'desc': "She is a little old lady with white hair and tint of purple. ",
					'intro':"Hello dear, I am Bethal Haut. I used to be Master Winston's nanny years ago. Still a good family friend. ",
					'converse':"YOU: I am ... I work at the Winston Corporation in Finance. BETHAL: Nice to meet you. ",
					'talkMore1': "Yes, I remember those days when Master Winston was a cute school boy. He was such a nice dear. ",
					'talkMore2': "Back when I was a young lady, I was quite the looker. My daddy had to chase the boys off with a rod. ",
					'talkMore3': "Even Master Winton's father ... um tried ... to get me to have drinks with him at times. ",
					'bless': "Bless your heart. "}
	properties = {'conversation':False, 'talkMore1': False, 'talkMore2': False, 'talkMore3': False}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']

	def talk(self):
		if self.properties['talkMore3']:
			return self.descriptions['talkMore3']
		elif self.properties['talkMore2']:
			self.properties['talkMore3'] = True
			return self.descriptions['talkMore2']
		elif self.properties['talkMore1']:
			self.properties['talkMore2'] = True
			return self.descriptions['talkMore1']
		elif self.properties['conversation']:
			self.properties['talkMore1'] = True
			return self.descriptions['converse']	
		else:
			self.properties['conversation'] = True
			return self.descriptions['intro']

	def touch(self):
		return self.descriptions['bless']

eng.setupItem(OldLady())
