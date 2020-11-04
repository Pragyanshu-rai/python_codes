from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

url=input("Enter - ")
urlh=urllib.request.urlopen(url).read()
soup=BeautifulSoup(urlh,'html.parser')
#print(type(soup))
tags=soup('a')
for tag in tags:
    print(tag.get('href',None))
