import string
def titletonumber(A):
    res=0
    str1=dict((key,0) for key in string.ascii_uppercase)
    i=1
    for key in string.ascii_uppercase :
        str1[key]=i
        i+=1
    for i in range(len(A)):
        if len(A)==1:
            return str1[A.upper()]
        else:
            str2=A[::-1].upper()
        res+=(str1[str2[i]]*(26**i))
    #print(3 in str1.values())
    return res
print(titletonumber(input("Enter a value\n>>")))
