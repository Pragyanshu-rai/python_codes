def afterBackspace(string):
 result=list()
 for ch in string:
  if ch == "#":
   result.pop()
  else:
   result.append(ch)
 res=""
 for char in result:
  res += char 
 return res

def compareTwoStrings(str1, str2):

 if afterBackspace(str1) == afterBackspace(str2):
  return 1
 return 0

print(compareTwoStrings("yf#c#", "yy#k#pp##"))
print("---------------------------------------------------")
print(compareTwoStrings("hacc#kk#", "hb##ackk##"))
