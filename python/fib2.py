import sys
number  = int(input())
array=list()
array.append(0)
array.append(1)
for num in range(2, number+1):
    array.append((array[num-1]+array[num-2])%10)
print(array[number])
