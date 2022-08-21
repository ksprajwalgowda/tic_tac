import requests
url = 'http://127.0.0.1:8000/hello/logout/'
# myobj = {
#     'old_password':'Hype#123',
#     'new_password':'Hype@123'
# }

x = requests.get(url, data = {}, headers = {"Authorization": "Token 6a37f170b87bb087d10cad38f4be53bb8afd4bd2"})
# print(x.text)
print(x)

# url = 'http://127.0.0.1:8000/hello/api-token-auth/'

# myobj = {
#     'username':'qwe' ,
#     'password':'Hype@123'
# }

# x = requests.post(url,data = myobj)
# print(x.text)