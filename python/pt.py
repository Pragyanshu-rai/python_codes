#def time(t):
#	assert t > 0, "time can't be negative"
#	print(f"the time is {t} o'clock")
#time(int(input("Enter the time \n")))
def t():
	for i in range(5):
		yield i*i
#a = t()
for i in t():
	print(i)
