number=int(input())
c=[[0 for x in range(number)]for y in range(number)]
p=list()
p.append((0,0))
top=0
bottom=number-1
left=0
right=number-1
element=1
while top<=bottom and left<=right:
    i=left
    while i<=right:
        c[top][i]=element
        if element%11==0:
            p.append((top,i))
        element+=1
        i+=1
    top+=1
    j=top
    while j<=bottom:
        c[j][right]=element
        if element%11==0:
            p.append((j,right))
        element+=1
        j+=1
    right-=1
    k=right
    while k>=left:
        c[bottom][k]=element
        if element%11==0:
            p.append((bottom,k))
        element+=1
        k-=1
    bottom-=1
    l=bottom
    while l>=top:
        c[l][left]=element
        if element%11==0:
            p.append((l,left))
        element+=1
        l-=1
    left+=1
for i in range(number):
    for j in range(number):
        print(c[i][j],end=" ")
    print()
print("Total Power points :",len(p))
for i in p:
    print(str(i).replace(" ",""))
print()
