t = "Apple Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that")
st = t.split(" ")
ms = ["day","night","song","frisbee","corn","banana","girl","boy"]
while len(st)!=10:
	n = ms.pop()
	print("Adding: ",n)
	st.append(n)
	print(f"There are {len(st)} items now.")
print("There we go: ",st)
#for i in st:
#+-	print(i)
print("Let's do some things with stuff.")
print(st[1])
print(st[-1])
print(st.pop())
print(' '.join(st))
print('#'.join(st[3:6]))
