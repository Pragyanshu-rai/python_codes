fn = input("Enter the file name -> ")
if len(fn) < 1 :
    fn = "mbox-short.txt"
lines = open(fn,"rt")
count = 0
for line in lines :
    line = line.rstrip()
    if line.startswith("From ") :
        temp = line.split()
        print(temp[1])
        count += 1
print("There were",count,"lines in the file with From as the first word")
