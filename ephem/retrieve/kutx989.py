import requests
from bs4 import BeautifulSoup as bs4
import lxml
from datetime import date
import calendar
import write



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
  day = wkshows()
  
  response = requests.get('https://api.composer.nprstations.org/v1/widget/50ef24ebe1c8a1369593d032/day', headers=headers, params=params)
  soup = bs4(response.text,'lxml')
  # print(soup)
  p_tags = soup.select('body p')[0]

  # print(p_tags.contents[0].string[0:2000])
  split_by_curly = p_tags.contents[0].string.split('{')
  dayt = []
  songs = {
    'dayt': {
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
      song = { 'station': 'kutx989'}
      split_by_comma = x.split(',')
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
        
      songs['dayt'][str(hour)].append([track, artist])  
      for show in day:
        if(int(hour) >= int(show["start"]) and int(hour) < int(show["end"])):
          song["show"] = show["title"]
          song["date"] = date.today().strftime('%Y-%m-%d')
          song["artist"] = artist
          song["track"] = track
          print(song)
          write.pg(song)
      #   print(show["start"], show["end"])
      # print(hour, track, artist)

  # # print(songs['date'])
  # print(songs['date'])
  # return songs['date']

def wkshows():
  day = []
  today = calendar.day_name[date.today().weekday()].lower()
  id = f"kutx-{today}"
  response = requests.get('https://kutx.org/program-schedule/', headers=headers, params=params)
  soup = bs4(response.text,'lxml')
  shows = soup.find("div", id=id).find_all("div", class_="kutx-schedule-list-item")
  for show in shows:
    name = show.find("div", class_="kutx-schedule-list-host")
    if(name):
      host = name.text
      title = show.find("div", class_="kutx-schedule-list-title").text
      begin = show.find("div", class_="kutx-schedule-list-time").text.split("-")[0].split(" ")
      if(begin[0] == 12 and begin[1] == "am"):
        start = 0
      elif(begin[1] == "am"):
        start = begin[0]
      elif(begin[0] == "12" and begin[1] == "pm"):
        start = 12
      elif(begin[1] == "pm" and begin[0] != 12):
        start = int(begin[0]) + 12
      
      fin = show.find("div", class_="kutx-schedule-list-time").text.split("-")[1].split(" ")
      if(fin[0] == 12 and fin[1] == "am"):
        end = 0
      elif(fin[1] == "am"):
        end = fin[0]
      elif(fin[0] == "12" and fin[1] == "pm"):
        end = 12
      elif(fin[1] == "pm" and fin[0] != 12):
        end = int(fin[0]) + 12
      
      day.append({
        'start': start,
        'end': end,
        'title': title,
        'host': host
      })

  return day
  

if __name__ == "__main__":
  main()

  # You can return data to show outputs to users.
    # Outputs documentation: https://docs.airplane.dev/tasks/outputs
    # return [
    #     {"songs": songs['date']}
    # ]
