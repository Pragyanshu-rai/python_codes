i=0
n=[]
def fu(i):
	print(f"At the top i is {i}")
	n.append(i)
	i+=1
	print("Numbers now :", n)
	print(f"At the bottom i is {i}")
	if i<6:
		fu(i)
fu(i)
print("The numbers: ")
for nu in n:
	print(nu)
