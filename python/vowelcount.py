string = input()

vowels={'a':0, 'e':0, 'i':0, 'o':0, 'u':0,}

for char in string:
    
    if vowels.get(char, -1) == 0:
        vowels[char] = 1

result=0

for value in vowels.values():
    
    result += int(value)

print(result)

number = "1"

count = 0

for char in number:
    
    if char != '0':
        count += 1

print(count)

