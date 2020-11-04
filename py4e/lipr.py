fn=input("Enter the file name: ")
lines=open(fn,"rt")
li=list()
for line in lines:
    line=line.rstrip()
    temp = line.split()
    for te in temp :
        if te in li :
            continue
        li.append(te)
li.sort()
print(li)
