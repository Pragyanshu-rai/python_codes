size = int(input())

count = 0
prev = None

for index in range(size):
    magnet=input()
    if index == 0:
        count += 1
        prev = magnet 
    elif prev != magnet:
        prev = magnet
        count +=1

print(count)
