size = input()

array=list(map(int, input().split()))

unique=dict()

for num in array:
    
    unique[num] = unique.get(num, 0) + 1

for key in unique.keys():
    
    if unique[key] == 1:
        print(key)


