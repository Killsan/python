import requests
import printer as pr
from bs4 import BeautifulSoup as bs

req = requests.get('https://vk.com/login')

print(req) #or print(dir(req))
#also you can use print(help(req))

