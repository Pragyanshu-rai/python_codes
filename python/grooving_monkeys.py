def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a>b:
        return gcd(a%b,b)
    if a<=b:
        return gcd(a,b%a)
def lcm(a,b):
    return (a*b)//gcd(a,b)
test_case=int(input())
for test in range(test_case):
    size = int(input())
    line = input()
    line = line.strip().split(" ")
    monkey=list()
    ticks=[1]
    for num in line:
        monkey.append(int(num)-1)
    for i in range(size):
        if monkey[i]==0:
            continue
        count=0
        block=0
        current=i
        while True:
            block=i
            temp=current
            current=monkey[current]
            monkey[temp]=0
            count+=1
            if current==block:
                if count not in ticks:
                    ticks.append(count)
                break
    res=ticks[0]
    for lcmn in range(1,len(ticks)):
        res=lcm(res,ticks[lcmn])
    print(res)
