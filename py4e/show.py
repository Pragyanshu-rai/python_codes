fname = input("Enter the file name : ")
if len(fname) == 0 :
    fname = 'mbox.txt'
file_handle = open(fname)
for line in file_handle:
    if not line.startswith('From'): 
        continue
    words = line.strip().split(" ")
    print("Email -",words[1])
