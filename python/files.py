fname = input("Enter The File Name: ")
if len(fname) < 1:
  fname="test.txt"
fhand = open(fname, "r")
opfile = open("out_"+fname, "w")

data = fhand.read().split("\n")
print(data)
data = data[::-1]

for line in data:
  line += " \n"
  opfile.write(line)

fhand.close()
opfile.close()

print("data transfer complete >", "out"+fname)