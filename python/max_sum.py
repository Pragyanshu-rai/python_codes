test_case=int(input())
for test in range(test_case):
    line=input()
    line=line.strip().split(" ")
    size=int(line[0])
    bags=int(line[1])
    array=input()
    array=array[::-1]
    array=array.strip().split(" ")
    if array[0]==min(array):
        array.reverse()
    max_no=int(array[0])
    op=list()
    for element in array:
        if bags==1:
            op.append(int(element))
        else :
            max_no=max(max_no,int(element))
            bags-=1
    max_no=max(max_no,sum(op))
    print(max_no)
