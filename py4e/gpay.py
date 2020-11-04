try :
	hrs=float(input("Enter Hours: "))
except :
	print("Enter A Number!!!!")
	hrs=float(input("Enter Hours(Number) : "))
try :
	rate=float(input("Enter The Rate Per Hour: "))
except :
	print("Enter A Numeric Value!!!!!")
	rate=float(input("Enter The Rate Per Hour(Number): "))
if(hrs>40):
    pay=rate*40
    pay+=rate*1.5*(hrs-40)
else :
    pay=rate*hrs
print(pay)
