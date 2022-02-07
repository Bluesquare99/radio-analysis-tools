import koop917schedule as show_schedule
import koop917_playlists as playlists
import re

def main():

	schedule = show_schedule.get_schedule()

	def clean_url(show_name):
		show_name_no_apostrophes = show_name.replace("'",'')		
		show_cleaned = re.sub('[^0-9a-zA-Z]+','-',show_name.replace("'",'').lower().strip())
		return show_cleaned

	for day in schedule:
		for k, v in schedule[day].items():
			# if(
			# 	# clean_url(v) == 'nobody-s-happy-hour' 
			# 	clean_url(v) == 'austin-artist-collective'
			# 	or clean_url(v) == 'bringing-light-into-darkness'
			# 	or clean_url(v) == 'lost-in-paradise-radio'
			# 	or clean_url(v) == 'the-sex-ed-show'
			# 	or clean_url(v) == 'the-austin-common-radio-hour'
			# 	or clean_url(v) == 'civil-rights-and-wrongs'
			# 	or clean_url(v) == 'off-stage-and-on-the-air'
			# 	or clean_url(v) == 'texas-music-office-s-texas-music-mixtape'
			# 	# or clean_url(v) == 'crate-digger-s-gold'
			# 	or clean_url(v) == 'the-stopped-clock'
			# 	or clean_url(v) == 'texchromosome-radio'
			# 	# or clean_url(v) == 'what-s-new'
			# 	or clean_url(v) == 'lights-camera-austin'
			# 	# or clean_url(v) == 'pearl-s-general-store'
			# 	or clean_url(v) == 'people-united'
			# 	or clean_url(v) == 'rag-radio'):
			# 	continue
			try:
				print(clean_url(v))
				print(playlists.get_playlist(clean_url(v)))
			except Exception as e:
				print(e)
		
# print(playlists.get_playlist(clean_url(v)))

if __name__ == "__main__":
	main()