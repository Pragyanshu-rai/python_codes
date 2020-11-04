def fact(a):
    print(a)
    if a==0:
        return 1
    else :
        return a*fact(a-1)
print(fact(5))
def fu(a,b):
    print(a,"\n",b)
fu(a=10,b=20)
fu(b=30,a=40)
def fu2(a,b=11):
    print(a,'\n',b)
fu2(2)
