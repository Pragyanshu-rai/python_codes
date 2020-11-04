a=lambda l,x:l**x 
print(a(2,3))
su=lambda q,w:q+w
print(su(10,20))
eod=lambda m:'yess' if m%2==0 else 'no'
print(eod(su(10,11)))
print("yesss") if a(2,3)==8 else print("nooooooo") #ternary operator
li=[1,2,3,4,5,6,7,8,9]
res1=list(filter(lambda s:s%2==0,li))
print(res1)
res2=list(map(lambda g:g*2,li))
print(res2)
from functools import reduce
res3=reduce(lambda l,h:h+l,li)
print(res3)
