import koop917_schedule
import koop917_playlists
import interact_with_pg
import re
from datetime import date
from dateparser import parse


def clean_url(show_name):
		show_name_no_apostrophes = show_name.replace("'",'')		
		show_cleaned = re.sub('[^0-9a-zA-Z]+','-',show_name.replace("'",'').lower().strip())
		return show_cleaned

def main():
	song_entry = {
		'station': 'koop917'
	}
	schedule = koop917_schedule.get_schedule()
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
				songs_played = koop917_playlists.get_playlist(clean_url(v))
				for artist, track in songs_played.items():
					song_entry['artist'] = artist or ''
					song_entry['track'] = track or ''
					interact_with_pg.write_to_pg(song_entry)
			except Exception as e:
				print('This error comes from koop917.py', e)
			finally:
				if(songs_played == None):
					print("It's reached none")
				print(song_entry)

if __name__ == "__main__":
	main()