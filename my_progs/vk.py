from bs4 import BeautifulSoup as bs
import requests
import os
os.system('clear')
def save_data(html):
	file = open('file.html', 'w')
	file.write(html)
	file.close()
def page():
	person_id = input('vk.com/')
	try:
		html_file = requests.get('https://vk.com/' + person_id).text
	except ImportError:
		print('You need to install "requests" and "bs4" modules')
	else:
		soup = bs(html_file, 'lxml')
		html = soup.prettify()
		title = soup.find('title').text
		if title == '404 Not Found':
			print('No account')
		else:
			save_data(html)
			print(f'{title} has been saved in file.html')
page()