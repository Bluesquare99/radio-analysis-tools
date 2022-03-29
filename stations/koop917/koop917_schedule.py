import requests
import bs4

def get_schedule():

	result = requests.get('https://koop.org/shows/', headers={'User-Agent': 'Mozilla/5.0'})

	soup = bs4.BeautifulSoup(result.text, "html.parser")
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

if __name__ == "__main__":
	main()
