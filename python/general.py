size = int(input())
seq = list(map(int, input().split()))

start = seq[0]
index = 1
pos=[0, 0]
pi=0

while index < size:
    
    if seq[index] > start:
        pos[0] = index
        start = seq[index]
    index += 1

start = seq[index-1]
pos[1] = index-1
index -= 2

while index >= 0:
    
    if seq[index] < start:
        pos[1] = index
        start = seq[index]
    
    index -= 1

res = pos[0]+(size-1-pos[1])
# pi is for the smallest
# pos[0] is for the largest
if res > 1 and pos[0] > pos[1]:
    res -= 1

print(res)#, pi, pos[0], pos[1])
