def FahrenheitOrCelsius(c, temp):

    return ((temp-32)*5)/9 if c == 1 else ((temp*9)/5)+32

print(FahrenheitOrCelsius(1, 91.40))
print(FahrenheitOrCelsius(2, 25))

def ReplaceCharacter(str, ch1, ch2):
    
    st = list(str)
    
    if len(st) == 0:
        return None
    
    for i in range(len(st)):
        
        if st[i] == ch1:
            st[i]=ch2
        elif st[i] == ch2:
            st[i]=ch1
    
    return "".join(st)

print(ReplaceCharacter('apples', 'a', 'p'))
print(ReplaceCharacter('bluecoloure', 'l', 'o'))

def RemoveAdjacentDuplicate(str):
    
    st = list(str)
    
    if len(st) == 0:
        return ""

    while True:
        hasDups = False
        s = e = None
        dupe = ""
        ls = st[0]

        for i in range(1, len(st)):
            
            if st[i] == ls:
                hasDups = True
                e = i
            elif e is not None and st[i] != ls:
                break
            
            ls = st[i]
            s = i if e is None else s 
        
        if e is not None:
            dupe = "".join(st)[s:e+1]
        
        if dupe != "":
            s = "".join(st).replace(dupe, "") 
            st = list(s)
                   

        if not hasDups:
            break
    
    return "".join(st)

print(RemoveAdjacentDuplicate('dassam'))
print(RemoveAdjacentDuplicate('dfbbbfgaaaahb'))
print(RemoveAdjacentDuplicate('qpaadbbd'))
