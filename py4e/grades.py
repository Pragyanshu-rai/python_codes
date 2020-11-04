try :
    score=float(input("Enter the score : "))
except : 
    print("Enter A float value between 0 and 1!!!!!")
    score=float(input())
if score <= 1 and score >= 0:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else :
        print("F")
else :
    print("Invalid Input!!!!")
