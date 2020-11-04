i=0
while i<21:
    print(i)
    i+=1
x=[int(l) for l in input("Enter two numbers: ").split()]
i=x[0]
while i<x[1]+1 :
    if i%2==1 :
        print(i)
    i+=1
z=int(input("Enter A Number To Display A Multiplication Table: "))
for i in range(1,11):
    print("{} X {} = {}".format(z,i,(i*z)))
li=[1,2,3,4,5,6,7,8,9,0]
for i in li :
    for m in li:
        if m==5 :
            break;
        print(m)
    print(i)
for i in range(1,21):
    if i%3==0 :
        continue
    print(i)
j=int(input("Enter an Even Number: "))
assert j%2==0, "Not An Even Number!!!"
print("The Given Number Is Even :)")
