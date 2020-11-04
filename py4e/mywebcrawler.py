from re import findall
import urllib.request, urllib.error, urllib.parse 
links=dict()
def mywebcrawler(url) :
    ex=0
    urlh=urllib.request.urlopen(url)
    for line in urlh :
        line=line.decode().rstrip().lstrip()
        print(line)
        wordsv=findall('<a href=".(.+)"',line)
        wordsk=findall('>(.+)</a>',line)
        if len(wordsk) > 0 and len(wordsv) > 0 :
            links[wordsk[0]]=wordsv[0]
    if len(links) > 0 :
        surl="file:///home/pragyanshu/Desktop/hcj"
        for k,v in links.items() :
            print("Link Found!!!",k,"-",v)
            d=input("\tDo you want to open it?[y/n]")
            if d == 'y':
                ex = 1
                mywebcrawler(surl+v)
            if ex == 1 :
                print("Shutting down the web scraper\n\t........done")
                exit()
    print("Shutting down the web scraper\n\t........done")
mywebcrawler('file:///home/pragyanshu/Desktop/hcj/index.html')
#mywebcrawler('https://careerkarma.com/blog/python-typeerror-int-object-is-not-callable/')
