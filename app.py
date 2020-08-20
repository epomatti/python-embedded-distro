import requests

r = requests.get('https://www.google.com.br')
print(r.status_code)