rn=range(10)
rr=range(2,20)
for i in rn:
    print(i,2,sep='&')#for a separating character
print("Break")
for i in rr:
    print(i)
li=[10,20,30]
b=bytes(li)
print(type(b))
ba=bytearray(li)
print(type(ba),'\n',ba[1])
di={1:"pragyanshu",2:"rai",'a':"hero"}
print(di)
print(di.items())
k=di.keys()
for i in k:
    print(i)
v=di.values()
for i in v:
    print(v)
l,m,n=[2,3,6]
print(l,m,n)
x=int(input("Please Enter The Number To Test :- "))
if x==0:
    print("Zero")
elif x%2==0:
    print("Even")
else :
    print("Odd")
x=[int(l) for l in input("Please Enter The Marks In The Subjects Respectively(Maths,Physics and Chemistry ) :- ").split()]
if x[0]<35 or x[1]<35 or x[2]<35:
    print("Failed")
else :
    y=(x[0]+x[1]+x[2])/3
    if y<=59:
        print("C")
    elif y<=69:
        print("B")
    else :
        print("A")
