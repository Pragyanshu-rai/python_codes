import requests
import sys
import json

choice = int(input("Send-1, Retrieve-2, Update-3, Partial_update-4, Delete-5 : "))

url = input("Enter A URL: ")

if len(url) == 0:
    print("No URL Given! Taking Default URL")
    url="http://127.0.0.1:8000/studentapi/"

def send(url):
    
    data = input("Enter The Data as {'key':'value', ...}: ")

    if len(data) > 0:
        data = eval(data)
    else:
        print("No Data Given! Taking Default Data")
        data={'name':'Priya', 'roll':6, 'branch':'LLB', 'section':'L1', 'year':'V'}
    
    print(data)
    
    json_data = json.dumps(data)
    
    urlh = requests.post(url=url, data=json_data)
    
    print("Data Sent!")
    
    print(urlh.json())
    
def retrieve(url):
    
    pk = input("Enter ID number: ")
    
    print("Looking for data.......")
    
    data = dict()
    
    if len(pk) > 0:
        
        data = {"id":int(pk)}
    
    print(data)
    
    data = json.dumps(data)
    
    print(data)
    
    urlh = requests.get(url=url, data=data)# or requests.get(url=url)
    
    print("Data Found!")
    
    print(urlh.json())
    

def update(url):
    
    data = input("Enter The Data as {'key':'value', ...}: ")

    if len(data) > 0:
        data = eval(data)
    else:
        print("No Data Given! Taking Default Data")
        data={'id':7, 'name':'Priya', 'roll':6, 'branch':'BBA-LLB', 'section':'L1', 'year':'V'}
    
    print(data)
    
    json_data = json.dumps(data)
    
    urlh = requests.put(url=url, data=json_data)
    
    print("Data Sent!")
    
    print(urlh.json())
    
def partial_update(url):
    
    data = input("Enter The Data as {'key':'value', ...}: ")

    if len(data) > 0:
        data = eval(data)
    else:
        print("No Data Given! Taking Default Data")
        data={'id':7, 'branch':'LLB'}
    
    print(data)
    
    json_data = json.dumps(data)
    
    urlh = requests.patch(url=url, data=json_data)
    
    print("Data Sent!")
    
    print(urlh.json())
    
    
def delete(url):
    
    data = input("Enter The Id: ")

    if len(data) > 0:
        data={"id":data}
    else:
        print("No Data Given! Taking Default Data")
        data={'id':7}
    
    print(data)
    
    json_data = json.dumps(data)
    
    urlh = requests.delete(url=url, data=json_data)
    
    print("Data Sent!")
    
    print(urlh.json())
    

if choice == 1:
    send(url)
elif choice == 2:
    retrieve(url)
elif choice == 3:
    update(url)
elif choice == 4:
    partial_update(url)
else:
    delete(url)

