import requests
from random_strings import random_string

headers = {
    'authority': 'api.mail.tm',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'tr-TR,tr;q=0.7',
    'origin': 'https://mail.tm',
    'referer': 'https://mail.tm/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

r = requests.get('https://api.mail.tm/domains', headers=headers)
print(r.status_code)
# print(r.json())

mail = f'{random_string(15)}'
passw = f'{random_string(10)}'
domain = r.json()["hydra:member"][0]["domain"]
# print(domain)
json_data = {
    'address': "{}@{}".format(mail, domain),
    'password': "{}".format(passw)
}

r = requests.post('https://api.mail.tm/accounts', headers=headers, json=json_data)
print(r.status_code)
# print(r.text)
