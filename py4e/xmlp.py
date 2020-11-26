from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as et
url=input("Enter the url\n>>")
urlh=urllib.request.urlopen(url).read()
soup_obj=BeautifulSoup(urlh,'html.parser')
tags=soup_obj("commentinfo")
SumOfCount=0
count=et.fromstring(str(tags[0]))
lst=count.findall("comments/comment")
for element in lst:
    SumOfCount=SumOfCount+int(element.find('count').text)
print(SumOfCount)
