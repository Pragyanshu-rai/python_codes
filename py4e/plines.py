fname = input("Enter the name of the file >>>> ")
try :
    fvar=open(fname)
except :
    print("Sorry cannot open the file!!!!");
    quit()
for line in fvar:
    line=line.rstrip()
    print(line.upper())
