l=20
def greet(a):
    def gr(a):
        a="Hello "+a
        return a
    return gr(a)
print(greet("Pragyanshu"))
def cal():
    x=10+20
    y=10-20
    z=10*20
    w=10/20
    v=10//20
    u=10**20
    return u,v,w,x,y,z
print(cal())
def show():
    global l
    l=10
    print(l)
show()
m=show
m()
print(type(m))
def fa(x):
    x=x+" hello"
    return x
def na():
    l="rai"
    return l
def na2():
    return fa("bhai")
print(fa(na()))
print(na2())
