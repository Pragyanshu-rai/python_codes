import requests
import json
#import web_send

url = "http://127.0.0.1:8000/"

def login(data):
    
    print(type(data), data)
    headers = {"Content-Type":"application/json", }# to to declare the content type
    res = requests.post(url=url+"get-token/", headers=headers, data=data)
    print("login - response:")
    print(res.json())
    print(type(res.json()))

def signup(data):
    
    print(type(data), data)
    res = requests.post(url=url+"api-signup/", data=data)
    print("signup - response:")
    print(res.json())
    print(type(res.json()))

def getdata():
    
    token = input("Enter Authentication token: ")
    id = input("Enter Id: ")
    if len(id) == 0:
        id = None
    data = {"id":id}
    header = {"Authorization":"Token "+token}
    data = json.dumps(data)
    print(type(data), data)
    res = requests.get(url=url+"studentapiauth/", headers=header, data=data)
    print("data - response:")
    print(res.json())
    print(type(res.json()))

def postdata():
    
    token = input("Enter Authentication token: ")
    data = {'name':'Priya', 'roll':6, 'branch':'LLB', 'section':'L1', 'year':'V'}
    data = json.dumps(data)
    header = {"Authorization":"Token "+token}
    print(type(data), data)
    res = requests.post(url=url+"studentapiauth/", headers=header, data=data)
    print("data - response:")
    print(res.json())
    print(type(res.json()))

def deletedata():
    
    token = input("Enter Authentication token: ")
    id = input("Enter Id: ")
    data = {"id":id}
    data = json.dumps(data)
    header = {"Authorization":"Token "+token}
    print(type(data), data)
    res = requests.delete(url=url+"studentapiauth/", headers=header, data=data)
    print("data - response:")
    print(res.json())
    print(type(res.json()))

username = input("Enter Username : ")

if len(username) < 1:
    username = "Pranshu"

password = input("Enter Password : ")

if len(password) < 1:
    password = "Sahil"

option = int(input("1- login\n2- signup\n3- get data\n4- post data\n5- delete data\n> "))

data = json.dumps({'username':username, 'password':password})

print("data:- ", data)

if option == 1:
    login(data)
elif option == 2:
    signup(data)
elif option == 3:
    getdata()
elif option == 4:
    postdata()
else:
    deletedata()


