import requests


url = "URL/api/auth/login"

session =requests.session()
payload = {'login': 'any', 'password': 'any'}
headers = {"Content-type": "application/json"}
response = session.post(url, data=payload, header=headers)
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')