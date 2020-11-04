import urllib.request, urllib.error, urllib.parse

fh=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fh:
    print(line.decode().strip())
counts=dict()
fh=urllib.request.urlopen('http://data.pr4e.org/page1.htm')
for line in fh:
    words=line.decode().split()
    for word in words:
        counts[word]=counts.get(word,0)+1
for word,count in counts.items():
    print(word,'-',count)
