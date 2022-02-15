import requests
import bs4
import lxml

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
    ('date', '2018-01-28'),
    ('format', 'json'),
)

def main():
  response = requests.get('https://api.composer.nprstations.org/v1/widget/50ef24ebe1c8a1369593d032/day', headers=headers, params=params)
  
  soup = bs4.BeautifulSoup(response.text,'lxml')
  p_tags = soup.select('body p')[0]

  # print(p_tags.contents[0].string[0:2000])
  split_by_curly = p_tags.contents[0].string.split('{')


  date = []

  songs = {
    'date': {
      '00':[],
      '01':[],
      '02':[],
      '03':[],
      '04':[],
      '05':[],
      '06':[],
      '07':[],
      '08':[],
      '09':[],
      '10':[],
      '11':[],
      '12':[],
      '13':[],
      '14':[],
      '15':[],
      '16':[],
      '17':[],
      '18':[],
      '19':[],
      '20':[],
      '21':[],
      '22':[],
      '23':[]
    }
  }

  for x in split_by_curly:
    if 'trackName' in x and not 'itunes' in x:
      split_by_comma = x.split(',')
      # print(split_by_comma)

      hour = ''
      track = ''
      artist = ''

      for i in split_by_comma:
        if 'start_time' in i:
          hour = i.split(' ')[1][0:2]
        if 'trackName' in i:
          track = i.split(':')[1].strip('"')
        if 'artistName' in i:
          artist = i.split(':')[1].strip('"')
        

      songs['date'][str(hour)].append([track, artist])  
      # print(f'{hour}, {track}, {artist}')

  # print(songs['date'])
  return songs['date']

if __name__ == "__main__":
  main()