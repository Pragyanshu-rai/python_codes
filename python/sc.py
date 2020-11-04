x = int(input())
li = []
y=input()
i=0
while y[i]!='\0':
	if y[i]!=' ':
		li.append(int(y))
key=0;
for i in range(x):
	if key<li[i] :
		key=li[i] 
aye=0;
for i in range(x):
	if (aye<li[i])and(li[i]<key):
		aye=li[i]
print(aye)
