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
#print(weights)
while done < len(weights):
    #print(i,j)
    if i==j:
        trips+=1
        done+=1
        i+=1
        weights[i]=7
        j=len(weights)-1
    elif done == len(weights)-1:
        #print(done,"alone element")
        done+=1
        trips+=1
        j+=1
    elif weights[i] > 1.5:
        i+=1
        trips+=1
        done+=1
        #print("Greater tha 1.5")
        continue
    elif weights[i]+weights[j] <= 3.00:
        weights[i]=7
        weights[j]=7
        trips+=1
        i+=1
        done+=2
        #print("sum < 3",weights)
    j-=1
print(trips)
