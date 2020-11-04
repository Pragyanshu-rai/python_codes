def p_two(*args):
    arg1, arg2 = args
    print(f"{arg1} {arg2}")
def p_one(a):
    print(a)
def p_twoa(a,b):
    print(a,b)
def p_none():
    print("I got nothin....") 
p_two("pragyanshu","rai")
p_twoa("priya","singh")
p_one("sahil")
p_none()
