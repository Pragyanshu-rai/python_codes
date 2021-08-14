import requests
from json import dumps
from os import environ

url = "https://maytapi-whatsapp.p.rapidapi.com/%7Bphone_id%7D/sendMessage"

payload = {
    "to_number": environ["MY_PHONE_NUMBER"],
    "type": "text",
    "message": "Hello"
}
payload = dumps(payload)
headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "2033a53a08mshb3a4b7f2d003de0p17dc37jsnb93fdf9f1b6e",
    'x-rapidapi-host': "maytapi-whatsapp.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)