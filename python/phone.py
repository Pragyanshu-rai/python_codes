size = int(input())
number = input()
eights = 0

total = size//11

for num in number:
    if num == "8":
        eights+=1

if eights >= total:
    print(total)
else:
    print(eights)

