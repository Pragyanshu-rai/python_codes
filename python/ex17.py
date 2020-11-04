from sys import argv
from os.path import exists
script, ff, tf = argv
print(f"copying from {ff} to {tf} file")
inf = open(ff)# can also be written a 'ind=open(ff).read()'
ind = inf.read()#then the file is not needed to be closed
print(f"The input file is {len(ind)} data long")
print(f"Does the output file exist? {exists(tf)}")
print("Ready, hit return to continue and ctrl-c to abort")
input()
of = open(tf,'w')
of.write(ind)
print("Alright, all done")
of.close()
inf.close()
