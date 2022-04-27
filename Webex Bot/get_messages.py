import requests

roomId = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYTg4MGY3NzAtYzVhNi0xMWVjLWFhNjQtMDlhMGJiYmZkOTFh'
token = 'NGUxZTk0MzgtMDNmZi00YzIwLWFhODEtNzM5OWQxNmE5YWJiZGJkMDIxYjItOTIy_P0A1_17ec3022-497d-4eb1-a4df-d430c60c5a4d'

url = "https://webexapis.com/v1/messages?roomId=" + roomId

header = {"content-type": "application/json; charset=utf-8",
         "authorization": "Bearer " + token}

response = requests.get(url, headers = header, verify = True)

print(response.json())
