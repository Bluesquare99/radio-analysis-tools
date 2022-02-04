import koop917schedule as show_schedule
import re

def main():

	schedule = show_schedule.get_schedule()
	# print(schedule['Monday'])

	def clean_url(show_name):
		return re.sub('[^0-9a-zA-Z]+','-',show_name.lower().strip())


	for day in schedule:
		for k, v in schedule[day].items():
			print(clean_url(v))
		

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