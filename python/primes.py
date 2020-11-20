def primesum(A):
    def isprime(x):
        n=2
        if x<=1:
   	        return False
        if x<=3 :
   	        return True
        while n<=x//2:
            if x%n==0:
                return False
            n+=1;
        return True
    ar=[];
    x=2;
    i=0;
    a=int(A)
    while x<=a//2 :
        if isprime(x):
            ar.append(x)
        x+=1
    for i in ar:
        if isprime(a-i):
            return i,a-i
    return None
print(primesum(184))
