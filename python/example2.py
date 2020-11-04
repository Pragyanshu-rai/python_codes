class stu:
	#static or class variable
	a =20
	def __init__(self,x):
		self.m=x
		print("m= ",self.m)
	@classmethod
	def get(cls):
		print("a= ",cls.a)
	@staticmethod
	def aget():
		print("This is class stu")
s=stu(12)
s1=stu(144)
stu.get()
stu.aget()
s.get()
s1.get()
s.aget()
s1.aget()
