
def getAllKLength(n, k, final):

 set = list()

 alpha = '#abcdefghijklmnopqrstuvwxyz';

 for index in range(1, n+1):
  set.append(alpha[index])
 
 getAllKLengthRec(set, "", n, k)

def getAllKLengthRec(set, prefix, n, k):

	if (k == 0) :
		final.append(prefix)
		return 

	for i in range(n):

		newPrefix = prefix + set[i]

		getAllKLengthRec(set, newPrefix, n, k - 1)

def getSmaller(string, final):
 op = list()
 for s in final:
  if s < string:
   op.append(s)
 
 return op

def isPal(string):
 if string == string[::-1]:
  return True
 return False

def getPalCount(final):
 count = 0;
 for string in final:
  if isPal(string) == True:
   count += 1
 return count 

def isValid(k, n, string, final):
 getAllKLength(k, n, final)
 # print(final)
 final = getSmaller(string, final)
 # print(final)
 count = getPalCount(final)
 return count

def output(id, k, n, string, final):
 count = isValid(k, n, string, final)
 print("Case #{}: {}".format(id, count))

repeat = int(input())
id=1
while repeat > 0:
 
 final = list()

 n, k = list(map(int, input().split()))
 string = input()

 output(id, k, n, string, final)
 id += 1
 repeat -= 1
