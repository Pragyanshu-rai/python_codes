import math
def isprime(number):
    if number<=1:
        return False
    if number<=3:
        return True
    if number%2==0:
        return False
    last=math.floor(math.sqrt(number))
    for num in range(3,last+1,2):
        if number%num==0:
            return False
    return True
def prime_range(number):
    prime_list=list()
    for num in range(number+1):
        if isprime(num):
            prime_list.append(num)
    return prime_list
def tobinary(number):
    result=''
    while number:
        result+=str(number%2)
        number//=2
    return result
test_case=int(input())
for test in range(test_case):
    special=0
    line=input()
    line=line.strip().split(" ")
    lower=int(line[0])
    upper=int(line[1])
    upper+=1
    for number in range(lower,upper):
        #string=bin(number)
        #string=string[::-1]
        prime_index=prime_range(32)
        for index in prime_index:
            if (1<<(index-1))&number==1<<index-1:
                special+=1
    print(special)
