# import requests
# url = 'http://127.0.0.1:8000/hello/userdetails/'
# myobj = {
#     'email':'ksprajwalgowda35@gmail.com',
#     'username':'prajwal',
#     'first_name':'prajwal',
#     'last_name':'gowda',
#     'dob': '2022-08-22',
#     'gender': 'male',
#     'bio':'dasdasdasdsdas',
#     'phone_no':'9481267125',
#     'uploaded_image': open('t.png')

# }

# x = requests.post(url, data = myobj, headers = {"Authorization": "Token 49df5227099f028dbd6b4d850f5c2efa396d2467"})
# print(x.text)
# print(x)

# url = 'http://127.0.0.1:8000/v1/auth/'

# myobj = {
#     'username':'admin' ,
#     'password':'123'
# }

# x = requests.post(url,data = myobj)
# print(x.text)


import sys
import requests
URL = 'http://127.0.0.1:8000/v1/auth/'
client = requests.session()

def getCookies(cookie_jar, domain):
    cookie_dict = cookie_jar.get_dict(domain=domain)
    found = ['%s=%s' % (name, value) for (name, value) in cookie_dict.items()]
    return ';'.join(found)
# Retrieve the CSRF token first
client.get(URL)  # sets cookie
print(client.cookies)
print(getCookies(client.cookies,'http://127.0.0.1:8000/'))
# if 'csrftoken' in client.cookies:
#     # Django 1.6 and up
#     csrftoken = client.cookies['csrftoken']
# else:
#     # older versions
#     csrftoken = client.cookies['csrf']

# # Pass CSRF token both in login parameters (csrfmiddlewaretoken)
# # and in the session cookies (csrf in client.cookies)
# EMAIL = 'admin'
# PASSWORD = '123'
# login_data = dict(username=EMAIL, password=PASSWORD, csrfmiddlewaretoken=csrftoken, next='/')
# r = client.post(URL, data=login_data, headers=dict(Referer=URL))