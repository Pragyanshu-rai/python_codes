from sys import argv
script , file1 = argv
t = open(file1)# to open the file file1 using t 
print(f"Here is your file {file1}")
print(t.read())# to read the contents of the file file1
#print("Type the filename again")
#filea = input("> ")
#ta = open(filea)
#print(ta.read())
