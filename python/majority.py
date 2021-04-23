size = int(input())
array=list(map(int, input().split()))

size //= 2
occur = dict()

for number in array:
    occur[number] = occur.get(number, 0)+1

value = "na"

for key in occur.keys():
    if occur[key] > size:
        value = key
        break

print(value)
