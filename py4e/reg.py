from re import findall
fn=input("Enter the file name : ")
try:
    lines=open(fn,'rt')
except:
    fn="ad.txt"
    print("File not found.....\nusing the file",fn)
    lines=open(fn,'rt')
number_list=list()
for line in lines:
    li=findall("([0-9]+)",line)
    for x in li:
        number_list.append(float(x))
m=sum(number_list)
print(int(m))
