array = list(map(int, input().split()))

op = list()

for num in array:
 if num not in op:
  op.append(num)

for num in op:
 print(num, end=" ")

print()
