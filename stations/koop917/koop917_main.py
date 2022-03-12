import koop917_schedule
import koop917_playlists
import re
from datetime import date
from dateparser import parse

def clean_url(show_name):
		show_name_no_apostrophes = show_name.replace("'",'')		
		show_cleaned = re.sub('[^0-9a-zA-Z]+','-',show_name.replace("'",'').lower().strip())
		return show_cleaned

def main():
	song_entry = {}

	schedule = koop917_schedule.get_schedule()
	for day in schedule:
		song_entry['date'] = parse(day, settings={'PREFER_DATES_FROM': 'past'}).strftime('%m %d %Y') or ''
		for k, v in schedule[day].items():
			song_entry['time'] = k or ''
			song_entry['show'] = v or ''
			try:
				songs_played = koop917_playlists.get_playlist(clean_url(v))
				song_entry['songs_played'] = songs_played or ''
				print(song_entry)
			except Exception as e:
				print('This error comes from koop917.py', e)
			finally:
				if(songs_played == None):
					print("It's reached none")
					song_entry['songs_played'] = ''
				print(song_entry)

if __name__ == "__main__":
	main()