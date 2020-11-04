li=[10,120.77,3,"hey saxy",[1,2,3,4],(11,22,33),"""
hey baby
how you doin....
""",15]
l2=li[0:3]
print(l2)
print(li)
print(len(li))
li.remove("hey saxy")
li.insert(0,69)
li.append(16)
#li.clear()#to delete all the elements from the list
del(li[6])
print(li)
print(max(l2),'\n',min(l2))
l2.sort()
print(l2)
l2.sort(reverse=True)
print("reverse - ",l2)
#tuple
tp=(69,88,56,24)
print(type(tp),'\n',tp)
l3=list(tp)
tp2=tuple(l2)
print(type(tp2),'\n',tp2)
print(type(l3),'\n',l3)
#sets
se={10,20,30,40,50,"hyyhyhy"}
se.update(["hey","bro"])
print(se)
se.remove(10)
print(se)
#fr=frozen(se)
#fr is a frozen set with the same values as the set se
