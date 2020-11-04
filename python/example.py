class computer:
	def __init__(self,ram,cpu):
		self.ram=ram
		self.cpu=cpu
	def config(self):
		print("ram: ",self.ram,"cpu: ",self.cpu)
c1=computer(4,'i5')
c1.config()
