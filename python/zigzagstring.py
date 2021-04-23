string = input()
off = int(input())
def zigzag(number, offset):
    move=0
    flag=True
    traverse=list()
    for num in range(number):
        traverse.append(move)
        if move == offset-1:
            flag = False
        if move == 0:
            flag = True
        if flag == True:
            move+=1
        else:
            move-=1
        
    return traverse

def convert(string, offset):
    result=["" for x in range(offset)]
    traverse=zigzag(len(string), offset)
    for index in range(len(traverse)):
        result[traverse[index]] +=string[index] 
    res=""
    for element in result:
        res += element
    return res 

print(convert(string, off))
