fname = input("Enter the file name >>>>> ")
try :
    fvar = open(fname)
except :
    print("Cannot open the file",fname,"!!!!!!!!!!")
    quit()
count=0
s=0
for line in fvar:
    line=line.rstrip()
    if "X-DSPAM-Confidence:" in line :
        count+=1
        s+=float(line[(line.find(":")+1):])
print("Average spam confidence:",s/count)
