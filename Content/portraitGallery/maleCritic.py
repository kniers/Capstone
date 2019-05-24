import eng

class MaleCritic:
	name = 'male critic'
	#type = 'Item'
	visible = True 
	aliases = ['critic', 'Bennings']
	descriptions = {'desc': "The critic is wearing suit and staring intently at one of the portraits. He has an expression on his face calculated to make him seem smarter than he actually is. He seems friendly, though.",
					'takeMC': "He's invested in the art. He doesn't want to go anywhere.",
					'touchMC': "You poke the critic. He's so interested in the painting he doesn't even notice.",
					'talkPortraits': "You ask the critic what he thinks about the portraits. He responds 'I find this portrait here particularly intriguing. The expression on this individual's face betrays vulnerability behind the imperious mask.'",
					'talkLandscape': "You ask the critic what he thinks about the landscape. He says 'The painting is bigger than it is good, in my estimation. That's not to say it isn't good. It is. It is just really, really, big.'",
					'talkStillLife': "You ask the critic what he thinks about the still life. He pauses to think for a moment, then says 'It seems out of place in this gallery. Most of these works are by artists who are at least somewhat recognized. But that one is by a no-name painter.'",
					'talkMcGuffin': "You say to the critic 'You know that statue in the ballroom? I think it's by Rodin.'\n\n'Rodin?' says the critic. 'Ah, what a genius. I must take a look.' The critic leaves for the ballroom.",
					'talkDefault': "The critic doesn't respond. Evidentally he doesn't want to talk about that.",
					'talkFemaleCritic': "'What's with your friend over there?' you ask. 'She fancies herself the last word when it comes to fashion, but her entire critical method consists of counting the number of colors you're wearing and complaining if you have more than two.'",
					'talkNone': "'How's it going?' you ask the critic. 'Oh, quite all right.' he responds. 'I was just admiring this piece of the late Emily Whittaker. It's no Rondin, but it is stimulating.'"}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		return self.descriptions['takeMC']


	def touch(self):
		return self.descriptions['touchMC']


	def talk(self, aboutMe):
		if aboutMe is portraits:
			return self.descriptions['talkPortraits']
		if aboutMe is landscape:
			return self.descriptions['talkLandscape']
		if aboutMe is stillLife:
			return self.descriptions['talkStillLife']
		if aboutMe is None:
			return self.descriptions['talkNone']
		if aboutMe is rodinStatue:
			currRoom = eng.getCurrentRoom()
			currRoom.items.remove('male critic')
			# bRoom = eng.getRoomByName('ballroom')
			# bRoom.items.add('male critic')
			return self.descriptions['talkMcGuffin']
		else:
			return self.descriptions['talkDefault']
			

maleCritic = MaleCritic()
eng.setupItem(maleCritic)
