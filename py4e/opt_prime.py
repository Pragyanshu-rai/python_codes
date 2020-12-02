import math
import time
def isprime(num):
    if num <=1:
        return False
    if num <=3:
        return True
    if num%2==0:
        return False
    last=math.floor(math.sqrt(num))
    for pnum in range(3,last+1,2):
        if num%pnum==0:
            return False
    return True
number=int(input("Enter the number\n>>"))
start = time.time()
for i in range(1,number+1):
    print("is",i,"prime :",isprime(i))
end=time.time()
print("The time taken to compute :",end-start)

