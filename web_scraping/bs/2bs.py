from bs4 import BeautifulSoup
import requests

html_file = requests.get('https://vk.com/').text
soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())
for meta in soup.head:
	print(meta)