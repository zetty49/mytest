import requests
from bs4 import BeautifulSoup as BS
import lxml






url = 'https://www.booking.com/?aid=2230186'
req = requests.get(url)
soup = BS(req.text, 'lxml')
print(soup)