from re import findall
from bs4 import BeautifulSoup
import os
import urllib.request, urllib.error, urllib.parse
main_pos=17
repeat=7
names=list()
def find_link(url,pos):
    global repeat,names
    if repeat == 4:
        names.append(findall("_by_([a-zA-Z]+).html",url)[0])   
    if repeat == 0:
        return 1
    url_handle=urllib.request.urlopen(url)
    soup=BeautifulSoup(url_handle,'html.parser')
    a_tags=soup('a')
    for tag in a_tags:
        if pos == 0:
            repeat-=1
            names.append(findall("_by_([a-zA-Z]+).html",str(tag.get('href',None)))[0])   
            find_link(str(tag.get('href',None)),main_pos)
            return 1
        pos-=1
find_link('http://py4e-data.dr-chuck.net/known_by_Mathu.html',main_pos)
#find_link("http://py4e-data.dr-chuck.net/known_by_Fikret.html",2)
#print(names[len(names)-1])
print(names[-1])
