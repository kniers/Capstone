import eng

class PictureFrame:
	name = 'picture frame'
	#type = 'Item'
	visible = False 
	aliases = ['frame', 'photo']
	descriptions = {'desc': "It's a picture of the butler in a frame. The maid is clutching it to her chest as she sleeps.",
					'takePF': "That would wake the maid up. You're not supposed to be up here, so you don't want that."}
	properties = {}
	
	
	def look(self):
		self.visible = True
		return self.descriptions['desc']
	
	
	def take(self):
		return self.descriptions['takePF']


	def touch(self):
		return self.descriptions['takePF']


	def eat(self):
		return self.descriptions['takePF']
			

pictureFrame = PictureFrame()
eng.setupItem(pictureFrame)
