import koop917schedule as show_schedule
import koop917_playlists as playlists
import re
from datetime import date
import csv

def main():

	schedule = show_schedule.get_schedule()

	def clean_url(show_name):
		show_name_no_apostrophes = show_name.replace("'",'')		
		show_cleaned = re.sub('[^0-9a-zA-Z]+','-',show_name.replace("'",'').lower().strip())
		return show_cleaned
	weekday = '';
	time = '';
	show = '';
	date_scraped = date.today()
	songs_played = ''

	with open('koop917.csv', mode='w') as csv_file:
		fieldnames = ['weekday','time','show','date_scraped','songs_played']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

		writer.writeheader()
		for day in schedule:
			weekday = day
			for k, v in schedule[day].items():
				time = k
				show = v
				try:
					songs_played = playlists.get_playlist(clean_url(v))
				except Exception as e:
					print('This error comes from koop917.py')
					print(e)
				finally:
					if(songs_played == None):
						print("It's reached none")
						continue
					writer.writerow({'weekday': day, 'time':time, 'date_scraped':date_scraped, 'show':show, 'songs_played':songs_played})

		


if __name__ == "__main__":
	main()

# WHAT NEXT
# 1 Create a simple Python script that can prove usefulness of Cron
# 3 Create a stations folder
#		Place within this each station's collection of scripts
#		I'll have to use the 
# Execute that via Cron to see where it gets you
# 2 Watch YouTube video on automating job for another interpretation of how to do so