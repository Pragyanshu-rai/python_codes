def cnc(chc,crc):
	print(f"'You have {chc} cheese!!'")#using f for format string 
	print(f"You have {crc} boxes of crackers!")
	print("'Man you can have a party!!'\n")
    #print("'Get a blanket.'\n")    
print("using values 20,30")
cnc(input(),30)#input() as an argument
print("or using variables aoch = 23, aocr = 36")
aoch = 23
aocr = 36
cnc(aoch,aocr)
print("we can even do math in them, '10+23,34+12'")
cnc(10+23,34+12)
print("or we can do both, 'aoch+20,aocr+33'")
cnc(aoch+20,aocr+33)   	
