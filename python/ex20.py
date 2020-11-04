from sys import argv
inf = argv[1]#argv[n] to get nth entry
def p_all(f):
	print(f.read())
def re(f):
	f.seek(0)
def pal(cl,f):
	print(cl,f.readline())
cf = open(inf)
print("lets print the whole file\n")
p_all(cf)
print("Now lest rewind\n")
re(cf)
print("lets print three lines\n")
l=1
pal(l,cf)
l+=1
pal(l,cf)
l+=1
pal(l,cf)
l+=1
pal(l,cf)
l+=1
pal(l,cf)
l+=1
pal(l,cf)
