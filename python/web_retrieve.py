import requests

url = input("Enter A URL: ")

if len(url) == 0:
    url="http://74f1f95b37f3.ngrok.io/student_data/"

print("Looking for data.......")

try :
    urlh = requests.get(url)# or requests.get(url=url)
except :
    print("[ERROR] Enter A Valid URL!s")

print("Data Found!")

print(urlh.json())


