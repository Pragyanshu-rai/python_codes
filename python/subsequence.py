num=int(input("Enter the size of the array\n>>"))
arr=list()
subarr=list()
for i in range(num):
    arr.append(int(input("->")))
num1=int(input("Enter the size of sub sequence array\n>>"))
for i in range(num1):
    subarr.append(int(input("->")))
value=[False for i in range(num1)]
i=0
j=0
while j < num:
    if subarr[i] == arr[j]:
        value[i]=True
        i+=1
    if i == num1:
        break;
    j+=1
if False in value:
    print(False)
else :
    print(value[0])
