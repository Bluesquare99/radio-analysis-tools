from selenium import webdriver
import time

def get_playlist(show_cleaned):

	url = 'https://koop.org/programs/' + show_cleaned
	PATH = '/Users/bluesquarez/Documents/Coding/Resources/chromedriver'
	driver = webdriver.Chrome(PATH)
	driver.get(url)


	playlist_raw = driver.find_element_by_class_name("js-programPlaylist")
	songs = playlist_raw.text.split('\n')
	playlist = {}

	for song in songs:
		song_split = song.split('-')
		artist = song_split[0].strip()
		track = song_split[1].split('(')[0].strip()
		playlist[artist] = track

	driver.quit()
	print(playlist)

def main():
	get_playlist('the-lounge-show')
	

if __name__ == "__main__":
	main()
