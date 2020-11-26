import json
import urllib.request, urllib.parse, urllib.error
api_key = False
if not api_key :
    api_key=42
    serviceurl="http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl="https://maps.googleapis.com/maps/api/geocode/json?"
address = input("Enter the address\n: ")
if len(address)<1:
    exit()
parameters = dict()
parameters['address'] = address
if api_key != False: parameters['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parameters)
print(parameters)
print('Retrieving',url)
urlh = urllib.request.urlopen(url)
data=urlh.read().decode()
try :
    js = json.loads(data)
except :
    js = None
if not js or 'status' not in js or js['status'] != 'OK':
    print("===== Failure To Retrieve =====\n",data)
    exit()
print(js['results'][0]['place_id'])
