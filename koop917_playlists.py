from selenium import webdriver
import time

def get_playlist(show_cleaned):

	url = 'https://koop.org/programs/' + show_cleaned
	PATH = '/Users/bluesquarez/Documents/Coding/Resources/chromedriver'
	driver = webdriver.Chrome(PATH)
	try:
		driver.get(url)
	except Exception as e:
		print(e)

	# if(driver.find_element_by_class_name("js-programPlaylist") == ''):
	# 	return
	try:
		playlist_raw = driver.find_element_by_class_name("js-programPlaylist")
		if(playlist_raw.text == ''):
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
		print(e)
	finally:
		driver.quit()

	

if __name__ == "__main__":
	print(get_playlist('nobodys-happy-hour'))