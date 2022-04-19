	# main() imports
import re
from datetime import date
from dateparser import parse

	# get_schedule() imports
import requests
import bs4
import lxml

	# get_playlist() imports
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def main():
	song_entry = {
		'station': 'koop917'
	}
	schedule = get_schedule()
	for day in schedule:
			# Retrieving date for today or past week
		if(parse(day).strftime('%m %d %Y') == parse("Today").strftime('%m %d %Y')):
			song_entry['date'] = parse(day).strftime('%m %d %Y') or ''
		else:
			song_entry['date'] = parse(day, settings={'PREFER_DATES_FROM': 'past'}).strftime('%m %d %Y') or ''
			# Retrieving playlist for each show 
		for k, v in schedule[day].items():
			# song_entry['time'] = k or ''
			song_entry['show'] = v or ''
			try:
				songs_played = get_playlist(clean_url(v))
				for artist, track in songs_played.items():
					song_entry['artist'] = artist or ''
					song_entry['track'] = track or ''
					# interact_with_pg.write_to_pg(song_entry)
			except Exception as e:
				print('This error comes from koop917.py', e)
			finally:
				if(songs_played == None):
					print("It's reached none")
				print(song_entry)
				return song_entry

def get_schedule():
	result = requests.get('https://koop.org/shows/', headers={'User-Agent': 'Mozilla/5.0'})
	soup = bs4.BeautifulSoup(result.text,'lxml')
	time_slots = soup.select('tbody tr')
	days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
	schedule = {
		'Sunday':{},
		'Monday':{},
		'Tuesday':{},
		'Wednesday':{},
		'Thursday':{},
		'Friday':{},
		'Saturday':{},
	}

	for slot in time_slots:
		shows = slot.select('.schedule-cell')
		# Skipping the first slot because it's just a marker of beginning of time slot
		for day, show in enumerate(shows):
			if show.select('.time'):
				time = show.select('.time')[0].getText()
				name = show.select('.show-name')[0].getText()
				schedule[days[day-1]][time] = name
				# print(f'On {days[day-1]} at {time} is {name}')

	# for day in schedule:
	# 	print(f'{day}: {schedule[day]}\n')
	return schedule

def clean_url(show_name):
		show_name_no_apostrophes = show_name.replace("'",'')		
		show_cleaned = re.sub('[^0-9a-zA-Z]+','-',show_name.replace("'",'').lower().strip())
		return show_cleaned

def get_playlist(show_cleaned):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("window-size=1920,1080")
	# chrome_options.add_argument("--disable-dev-shm-usage")
	# chrome_options.add_argument("--no-sandbox")

	url = 'https://koop.org/programs/' + show_cleaned
	driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
	try:
		driver.get(url)
	except Exception as e:
		print("URL didn't open", e)

	try:
		playlist_raw = driver.find_element_by_class_name("js-programPlaylist")
		if(playlist_raw.text == ''):
			print(f'{show_cleaned} is likely a musical show but playlist is not shown')
			return
		songs = playlist_raw.text.split('\n')
		playlist = {}
		for song in songs:
			song_split = song.split('-')
			artist = song_split[0].strip()
			track = song_split[1].split('(')[0].strip()
			playlist[artist] = track

		return(playlist)
	except Exception as e:
		print(f'The program {show_cleaned} does not have a playlist and is therefore likely not a musical show')
	finally:
		driver.quit()

if __name__ == "__main__":
	main()