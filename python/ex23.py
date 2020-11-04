import sys
scr, encoding, error = sys.argv
def main(lf,encoding,errors):
	li = lf.readline()
	if li:
		pl(li,encoding,errors)
		return main(lf,encoding,errors)
def pl(li,encoding,errors):
	nl = li.strip()
	rb = nl.encode(encoding, errors=errors)
	cs = rb.decode(encoding, errors=errors)
	print(rb,"<==>",cs)
la = open("text.txt",encoding="utf-8")
main(la, encoding, error)
