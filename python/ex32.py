c = [1,2,3,4,5]
f = ['apple','oranges','pears','apricots']
ch = [1,'pennies',2,'dimes',3,'quarters']
for n in c:
	print("This is count {}".format(n))
for fs in f:
	print("A fruit of type: {}".format(fs))
for i in ch:
	print(f"I got {i}")
e = []
for i in range(0, 3):
	print(f"Adding {i} to the list")
	e.append(i)
for i in e:
	print("Element was: {}".format(i))
