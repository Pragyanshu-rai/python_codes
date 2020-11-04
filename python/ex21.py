def add(a,b):
	print(f"ADDING '{a} + {b}'")
	return a+b
def sub(a,b):
	print(f"SUBTRACTING '{a} - {b}'")
	return a-b
def mul(a,b):
	print(f"MULTIPLY '{a} * {b}'")
	return a*b
def div(a,b):
	print(f"DIVIDE '{a} / {b}'")
	return a/b#a//b for int result
print("Lets do some maths using functions!")
ag = add(30,5)
h = sub(78,4)
w = mul(90,2)
iq = div(100,2)
print(f"age:- {ag}, height:- {h},weight:- {w},IQ:- {iq}")
print("puzzle")
what = add(ag,sub(h,mul(w,div(iq,2))))
print(what)
