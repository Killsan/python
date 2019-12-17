from bs4 import BeautifulSoup as bs
import requests
import os
os.system('clear')

html_file = requests.get('https://vk.com').text
soup = bs(html_file, 'lxml')

print(soup.prettify())