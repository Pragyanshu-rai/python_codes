# Enter the input line by line not in a single line !!!!!
num=int(input())
x=None
row=[0 for i in range(num)]
col=list()
order=[-1 for i in range(num)]
swap=0
left=list()
for i in range (0,num):
    for j in range(0,num):
        x=input().lower()
        if x=='r':
            row[j]+=1
            order[i]=j+1
for i in range(num):
    if row[i]>(num-i):
        print(-1)
        exit()
    if i+1 not in order:
        left.append(i+1)
    if order[i]==-1:
        col.append(i)
for i in range(len(left)):
    order[col[i]]=left[i]
for i in range(num): 
    for j in range(i + 1,num): 
        if (order[i] > order[j]): 
            swap += 1
print(swap)
