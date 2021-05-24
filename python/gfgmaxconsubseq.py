# Python program to find longest contiguous subsequence


def findLongestConseqSubseq(arr, n):
 s = set()
 ans = 0
 msf = 0
 x=-1
 marr=list()
 for ele in arr:
		s.add(ele)
 for i in range(n):
		if (arr[i]-1) not in s:
			j = arr[i]
   x = j
   while j in s :
  	 j += 1
   ans = max(ans, j-arr[i])
   if msf < ans:
    marr.clear()
    while x in s :
     marr.append(x)
     x+=1
   msf = ans
	return marr


# Driver code
if __name__ == '__main__':
	n = 7
	arr = [1, 9, 3, 10, 4, 20, 2]
	print ("Length of the Longest contiguous subsequence is "),
	print (findLongestConseqSubseq(arr, n))

# Contributed by: Harshit Sidhwa
