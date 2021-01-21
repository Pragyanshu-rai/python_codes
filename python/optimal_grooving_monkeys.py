def gcd(a,b):
    if a== 0:
        return b
    if b==0:
        return a
    if a>b:
        return gcd(a%b,b)
    if a<=b:
        return gcd(a,b%a)
test_case=int(input())
for test in range(test_case):
    i=0
    tick=1
    position=list()
    size=int(input())
    line=input()
    line = line.strip().split(" ")
    for num in line:
        position.append(int(num))
    while i<size:
        temp=i
        j=0
        while position[i]!=0:
            temp2=i
            i=position[i]-1
            position[temp2]=0
            j+=1
        i=temp+1
        if j!=0:
            tick=tick*j/gcd(tick,j)
    print(int(tick))
