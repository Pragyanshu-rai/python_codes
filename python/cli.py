from sys import argv
lst=argv
for i in lst:print(i)
x=int(argv[1])
y=int(argv[2])
print("{} X {} = {}".format(x,y,(x*y))) 
print(argv)
