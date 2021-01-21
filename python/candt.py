def cat(lt):
    cmx = [0, 0, 0]
    cmn = [0, 0, 0]
    tmx = [0, 0, 0]
    tmn = [0, 0, 0]
    cf,tf = -1, -1
    for i in range(1,len(lt)-1):
        if (lt[i-1]<lt[i]>lt[i+1]):
            a = lt[i] - max(lt[i+1],lt[i-1])
            b = lt[i] - min(lt[i+1],lt[i-1])
            if cmx == [0, 0, 0]:
                cmx = [i, b, a]
                cmn = [i, b, a]
                cf = 0
                continue
            if a<cmn[2]:
                cmn = [i, b, a]
            if b>cmx[1]:
                cmx = [i, b, a]
        elif (lt[i-1]>lt[i]<lt[i+1]):
            a = min(lt[i+1],lt[i-1]) - lt[i]
            b = max(lt[i+1],lt[i-1]) - lt[i]
            if tmx == [0, 0, 0]:
                tmx = [i, b, a]
                tmn = [i, b, a]
                tf = 0
                continue
            if a<tmn[2]:
                tmn = [i, b, a]
            if b>tmx[1]:
                tmx = [i, b, a]
    if (cf+tf)!= 0:
        print(-1)
    elif (cf+tf) == 0:
        d = max(abs(cmx[0]-cmn[0]),abs(tmx[0]-tmn[0]))
        print(d)

t = int(input(''))
lt = []
for i in range(t):
    n = int(input(''))
    lt.append(list(map(int, input('').split(' '))))
for i in lt:
    cat(i)
