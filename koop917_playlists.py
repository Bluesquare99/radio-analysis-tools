from selenium import webdriver

PATH = '/Users/bluesquarez/Documents/Coding/Resources/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')
print(driver.title)
driver.quit()












# import requests
# import bs4
# import lxml

# def get_playlist(show_cleaned):

# 	url = 'https://koop.org/programs/' + show_cleaned + '/#playlists'
# 	result = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
# 	print(result)
# 	soup = bs4.BeautifulSoup(result.text,'lxml')
# 	print(soup.prettify())


# def main():
# 	get_playlist('the-lounge-show')
	

# if __name__ == "__main__":
# 	main()
