def toroman(number):
    m=['','M','MM','MMM']   
    c=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    x=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    i=['','I','II','III','IV','V','VI','VII','VIII','IX']
    th=m[number//1000]
    number%=1000
    hun=c[number//100]
    number%=100
    ten=x[number//10]
    number%=10
    return th+hun+ten+i[number]
print(toroman(1234))
