fn=input("Enter the file name : ")
try :
    lines=open(fn,'rt')
except :
    fn="mbox-short.txt"
    print("File not found.......\ntaking the default file",fn)
    lines=open(fn,'rt')
words=dict()
for line in lines:
    line=line.rstrip()#it is useless as the split function removes white spaces also
    li = line.split()
    if line.startswith('From '):
        words[li[1]]=words.get(li[1],0)+1
mx=0;
key=None
for word in words:
    if words[word] > mx :
        key=word
        mx=words[key]
print(key,words[key])
print(dir(words))
for (k,v) in words.items():
    print("words["+k+"] =",v)
