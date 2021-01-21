test_case=int(input())
for test in range(test_case):
    size=int(input())
    line = input()
    line = line.strip().split(" ")
    minci=-1
    maxci=-1
    minti=-1
    maxti=-1
    max_c=-1
    max_t=-1
    min_c=9999999999
    min_t=9999999999
    numbers=list()
    y=list()
    x=list()
    for number in line:
        numbers.append(int(number))
        y.append(int(number))
        x.append(int(number))
    x.sort()
    if max(numbers) == min(numbers) or y == x:
        print(-1)
        continue
    for i in range(1,size-1):
        if numbers[i-1] > numbers[i] < numbers[i+1]:
            if numbers[i-1]-numbers[i]>=max_t or numbers[i+1]-numbers[i]>=max_t:
                if numbers[i-1]-numbers[i]>numbers[i+1]-numbers[i]:
                    max_t = numbers[i-1]-numbers[i]
                else :
                    max_t = numbers[i+1]-numbers[i]
                maxti=i
            if numbers[i-1]-numbers[i]<min_t or numbers[i+1]-numbers[i]<min_t:
                if numbers[i-1]-numbers[i]<numbers[i+1]-numbers[i]:
                    min_t = numbers[i-1]-numbers[i]
                else :
                    min_t = numbers[i+1]-numbers[i]
                minti=i
        elif numbers[i-1] < numbers[i] > numbers[i+1]:
            if numbers[i]-numbers[i-1]>=max_c or numbers[i]-numbers[i+1]>=max_c:
                if numbers[i]-numbers[i-1]>numbers[i]-numbers[i+1] :
                    max_c = numbers[i]-numbers[i-1]
                else:
                    max_c = numbers[i]-numbers[i+1]
                maxci=i
            if numbers[i]-numbers[i-1]<min_c or numbers[i]-numbers[i+1]<min_c:
                if numbers[i]-numbers[i-1]<numbers[i]-numbers[i+1]:
                    min_c = numbers[i]-numbers[i-1]
                else:
                    min_c = numbers[i]-numbers[i+1]
                minci=i
    if minci==-1 or minti==-1 or maxci==-1 or maxti==-1:
        print(-1)
    else :
        print(max(maxti-minti,maxci-minci))

    numbers.clear()
