import requests

headers = {
    'authority': 'api.composer.nprstations.org',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
    'origin': 'https://kutx.org',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://kutx.org/',
    'accept-language': 'en-US,en;q=0.9',
}

params = (
    ('date', '2022-01-31'),
    ('format', 'json'),
)

def main():
  response = requests.get('https://api.composer.nprstations.org/v1/widget/50ef24ebe1c8a1369593d032/day', headers=headers, params=params)
  print(response.text)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://api.composer.nprstations.org/v1/widget/50ef24ebe1c8a1369593d032/day?date=2022-01-31&format=json', headers=headers)

if __name__ == "__main__":
  main()