trips=0
weights=list()
bags=int(input())
line=input()
temp=line.strip().split(" ")
for weight in temp:
    if float(weight) >= 2.0:
        trips+=1
    else:
        weights.append(float(weight))
weights.sort()
j=len(weights)-1
i=0
done=0
#print(len(weights))
while done < len(weights):
    if i == len(weights):
        break
    if weights[i] == 7:
        i+=1
    elif i==j:
        trips+=1
        done+=1
        i+=1
        weights[i]=7
        j=len(weights)-1
    elif done == len(weights)-1:
        print("alone element")        
        weights[i] = 7
        done+=1
        trips+=1
        j+=1
    elif weights[i] > 1.5:
        weights[i] = 7
        i+=1
        trips+=1
        done+=1
        print("Greater than 1.5",weights[i])
        continue
    elif weights[i]+weights[j] <= 3.00:
        weights[i]=7
        weights[j]=7
        trips+=1
        i+=1
        done+=2
        print("sum < 3",weights)
    print(weights[i],weights[j],i,j)
    j-=1
print(weights,trips)
