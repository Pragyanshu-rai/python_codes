import math
from time import time
def isprime(x):
    if x<=1:
   	    return False
    if x<=3 :
   	    return True
    last=math.floor(math.sqrt(x))
    for number in range(3,last+1,2):
        if x%number==0:
            return False
    return True
def primerange(lower,upper):
    primelist=list()
    for number in range(lower,upper+1,2):
        if isprime(number):
            primelist.append(number)
    return primelist
cur=time()
l=int(input())
u=int(input())
print(primerange(l,u),"\n",time()-cur)
