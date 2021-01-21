import math
import time
number=int(input("Enter the number\n>>"))
start=time.time()
factors=list()
for num in range(1,math.floor(math.sqrt(number))+1):
    if number%num==0:
        factors.append(num)
        factors.append(number//num)
factors.sort()
end=time.time()
for factor in factors:
    print(factor,end=" ")
print("\n",end-start,"\n")
