import eng

class Children:
	name = 'children'
	#type = 'Item'
	visible = True 
	aliases = ['kids']
	descriptions = {'desc': "There are three children playing with toys. They look like they are have an interesting conversations. Maybe we can LISTEN in. ",
					'listenMore':"That's lame I really wanted to see them eat. Sharks are so cool! Maybe we could find the key ourselves? ",
					'sharks': "Yeah, my grandpa keeps sharks in the basement, but we can't get in there without a key, sucks. ",
					'roomKey': "Grandpa keeps the key hidden somewhere in the bar. It's really creepy. It is made out of bone. Anyways we should avoid going in there without Grandpa. Last time I went in there alone, he got really mad. ",
					'converse': "Stranger danger!!! "}
	properties = {'listened':False, 'listenAll':False}
	
	
	def look(self):
		return self.descriptions['desc']

	def talk(self):
		return self.descriptions['converse']	

	def listen(self):
		if self.properties['listened'] == False:
			self.properties['listened'] = True
			return self.descriptions['sharks']
		elif self.properties['listenAll'] == False:
			self.properties['listenAll'] = True
			return self.descriptions['listenMore']
		else:
			return self.descriptions['roomKey']

children = Children()
eng.setupItem(children)
