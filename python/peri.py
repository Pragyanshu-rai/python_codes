import math
repeat=int(input())
per=0
list_dist=list()
x,y=map(int, input().split())
x2=x
y2=y
while repeat > 1 :
    dist=0
    x1,y1=map(int, input().split())
    dist=math.sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1))
    list_dist.append(dist)
    per+=dist
    x=x1
    y=y1
    repeat-=1
dist=math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
per+=dist
list_dist.append(dist)
print(max(list_dist))
