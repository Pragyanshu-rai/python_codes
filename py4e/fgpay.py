def fgpay(h,r):
    if h > 40:
        pay=rate*40
        pay+=rate*1.5*(h-40)
    else :
        pay=rate*h
    return pay
hr = float(input("Hours : "))
rate = float(input("rate : "))
print("Pay",fgpay(hr,rate))
