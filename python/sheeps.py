
def give_moves():

    n = int(input())
    a = input().strip()
    b = []
    for i in range(n):
        if a[i] == '*':
            b.append(i)
        if len(b) == 0:
            print(0)
            return

    c = b[len(b)//2]
    m = len(b)//2
    r = 0
    for i in range(1, m + 1):
        r += c-i-b[m-i]
    for i in range(1, len(b)-m):
        r += b[m+i]-c-i
    print(r)


repeat = int(input())

while repeat > 0:

    give_moves()
    repeat -= 1


