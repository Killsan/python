from bs4 import BeautifulSoup
import requests
import os 
def printer(obj):
	length = int(len(obj))
	print('-'*length)
	print(obj)
	print('-'*length)
os.system('clear')
with open('test.html') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')
# print(soup.prettify())
# match = soup.div
# match = soup.find('div')
# match = soup.find('nav', class_='header')
div_href = soup.find('div').a['href'] #link to the videos			
printer(div_href)
href_advanced = div_href.split('/') #info about link
# print(href_advanced)
href_advanced = div_href.split('/')[3] #full link to the video
# print(href_advanced)
href_advanced = div_href.split('?') #other info about the link
# print(href_advanced)
href_advanced = div_href.split('?')[1] #the id of the video
print(href_advanced)