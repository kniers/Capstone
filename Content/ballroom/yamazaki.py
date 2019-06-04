import eng

class Yamazaki:
	name = 'Yamazaki'
	#type = 'Item'
	visible = True 
	aliases = ['yamazaki', 'Mr. Yamazaki', 'Genzo Yamazaki', 'Japanese businessman']
	descriptions = {'desc': "You see an Japanese businessman dressed in formal attire. ",
					'intro':'Hajimemashite, I am Genzo Yamazaki. I am COO at Matsui Corp."',
					'converse':"YOU: I am ... I work at the Old Money Corporation in Finance. Yamazaki: Nice to meet you. Here is my business card. ",
					'shock': "Please sir do not touch me, it is not appropriate as business partners. "}
	properties = {'conversation':False}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']

	def talk(self):
		if self.properties['conversation']:
			currRoom = eng.getCurrentRoom()
			meishi = eng.getItemByName('business card')
			if meishi is not None:
				meishi.visible = True
				if meishi.properties['have'] == False:
					meishi.properties['have'] = True
					eng.addToInventory(meishi)
					return self.descriptions['converse']	
		else:
			self.properties['conversation'] = True
			return self.descriptions['intro']

	def touch(self):
		return self.descriptions['shock']


yamazaki = Yamazaki()
eng.setupItem(yamazaki)
