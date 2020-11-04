from sys import argv
script , file1 = argv
print(f"we're going to erase {file1}")
print("If you don't want tha then hit ctrl-c (^c).")
print("If you do want that then hit return.")
input("?")
print("Opening the file....")
t = open(file1,'w+')
print("Truncating the file. Goodbye!")
t.truncate()
print("Now I'm going to ask you to write in the file. enter 123 to exit")
x=input()
while x!='123':
   if x=='\n':
      t.write('\n')
   else :
      t.write(x)
   x=input() 
#print(t.read())
print(f"closing the file {file1}")
t.close()
