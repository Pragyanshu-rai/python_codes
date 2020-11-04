def br(st):#use help(ex25) to print V line below 
	""" This function will break up words for us."""
	w = st.split(' ')
	return w
def sort(w):#use from ex25 import * to import everything
	"""Sorts the words."""
	return sorted(w)
def pfw(w):
	"""Prints the first word after popping it off."""
	ws = w.pop(0)
	print(ws)
def plw(w):
	"""Prints the last word after popping it off."""
	ws = w.pop(-1)
	print(ws)
def ss(s):
	"""Takes in a full scentence ans returns the sorted words."""
	w = br(s)
	return sort(w)
def pfl(s):
	"""Prints the first and  last words of the scentence."""
	w = br(s)
	pfw(w)
	plw(w)
def pfls(s):
	"""Sorts the words then prints the first and last one."""
	w = ss(s)
        pfw(w)
	plw(w)
