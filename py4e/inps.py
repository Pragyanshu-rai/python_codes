ave = 0
s = 0
while True :
    x = input("Enter The Number: ")
    if x == "Done" :
        break
    try :
        s += float(x)
        ave += 1
    except :
        print("Invalid Input!!!!")
        continue;
print(s,s/ave)
