fn=input("Enter the file name: ")
try:
    lines=open(fn,'rt')
except:
    fn="mbox-short.txt"
    print("File not found....\nusing the default file \"",fn,"\"")
    lines=open(fn,'rt')
words=list()
time=list()
hrs=dict()
for line in lines:
    line=line.rstrip()
    words=line.split()
    if line.startswith("From "):
        time=words[5].split(":")
        hrs[time[0]]=hrs.get(time[0],0)+1
time.clear()
time=[(k,v) for k,v in hrs.items()]
time.sort()
for k,v in time:
    print(k,v)
