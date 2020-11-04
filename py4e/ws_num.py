from re import findall
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

url_handle=urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_988437.html")
soup=BeautifulSoup(url_handle,'html.parser')

span_tag=soup('span')
numbers=list()
for number in span_tag:
    numbers.append(int((findall(">([0-9]+)</span>",str(number)))[0]))
print(sum(numbers))
