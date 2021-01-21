import math
def isprime(num):
    if num <=1:
        return False
    if num <=3:
        return True
    if num%2==0:
        return False
    last = math.floor(math.sqrt(num))
    for number in range(3,last+1,2):
        if num%number == 0:
            return False
    return True
def toDecimal(num,base):
    baseNo="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num=num.upper()
    power=0
    result=0
    num=num[::-1]
    for char in num:
        result+=baseNo.find(char)*(base**power)
        power+=1
    return result
def toBase(number,base):
    baseNo="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result=""
    while number>=base:
        result+=baseNo[number%base]
        number=number//base
    result+=baseNo[number]
    result=result[::-1]
    return result
test_case=int(input())
for test in range(test_case):
    baseNo="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_base=0
    upper_base=0
    start=0
    line = input()
    line=line.upper()
    line = line.strip().split(" ")
    for char in line[0]:
        lower_base=max(lower_base,baseNo.find(char)+1)
    upper_base=baseNo.find(line[1])
    start=toDecimal(line[0],lower_base)
    upper_base+=1
    while True:
        if isprime(start)==True and line[1] in toBase(start,upper_base):
            print(toBase(start,upper_base))
            break
        start+=1
