import koop917schedule as show_schedule
import koop917_playlists as playlists
import re

def main():

	schedule = show_schedule.get_schedule()
	# print(schedule['Monday'])

	def clean_url(show_name):
		return re.sub('[^0-9a-zA-Z]+','-',show_name.lower().strip())


	for day in schedule:
		for k, v in schedule[day].items():
			if(clean_url(v) == 'nobody-s-happy-hour' 
				or clean_url(v) == 'austin-artist-collective'
				or clean_url(v) == 'bringing-light-into-darkness'
				or clean_url(v) == 'lost-in-paradise-radio'
				or clean_url(v) == 'the-sex-ed-show'
				or clean_url(v) == 'the-austin-common-radio-hour'
				or clean_url(v) == 'civil-rights-and-wrongs'
				or clean_url(v) == 'off-stage-and-on-the-air'
				or clean_url(v) == 'texas-music-office-s-texas-music-mixtape'
				or clean_url(v) == 'crate-digger-s-gold'
				or clean_url(v) == 'the-stopped-clock'
				or clean_url(v) == 'texchromosome-radio'
				or clean_url(v) == 'what-s-new'
				or clean_url(v) == 'lights-camera-austin'
				or clean_url(v) == 'pearl-s-general-store'
				or clean_url(v) == 'people-united'
				or clean_url(v) == 'rag-radio'):
				continue
			print(clean_url(v))
			print(playlists.get_playlist(clean_url(v)))
		
# print(playlists.get_playlist(clean_url(v)))

if __name__ == "__main__":
	main()

# XX Create a variable to hold each day and time slot
# You have the schedule--now you need to find the playlist for each function
#	This will require another scraping script
#	This next scraping script will have to dynamically register the urls and their extensions
#	Clean up the titles of the shows then use those to get the scripts
#
#	1. XX Start simple, start with one address
#		See how the url is composed
#		It's lower-cased, trimmed, all non-alphanumerics are replaced with -
#	2. XX Make soup
#	3. Create a function to get that playlist
#	4. Separate that function out in another file