print("Let's practice everything.")
print('you\'d need to know \'bout escapes with \\ that do:')
print("\n newlines and \t tabs")
poem ="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print("-----------")
print(poem)
print("-----------")
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")
def sf(s):
	jb = s * 500
	j = jb / 1000
	c = j / 100
	return jb,j,c
sp = 10000
b, j, c = sf(sp)
print("With a starting point of {}".format(sp))
print(f"We'd have {b} beans, {j} jars, and {c} crates.")
sp /= 10# can be also written as 'sp = sp / 10'
print('We can also do this this way')
f = sf(sp)
print("We'd have {} beans, {} jars, and {} crates.".format(*f))#*f means the same as argv or args
