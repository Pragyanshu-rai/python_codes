import json
import urllib.request, urllib.parse, urllib.error
url = input("Enter the url\n>>")
data = urllib.request.urlopen(url).read()
data_str=json.loads(data)
count_sum=0
for element in data_str['comments']:
    count_sum+=int(element['count'])
print(count_sum)
