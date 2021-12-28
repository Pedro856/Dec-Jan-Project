#Making imports
import urllib3
import requests
from bs4 import BeautifulSoup

page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')
# html = list(soup.children)[2]
# body = list(html.children)[3]
# p = list(body.children)[1]
# print(p.get_text())
###
# print(soup.find_all('p')[0].get_text())
###
# print(soup.find('p'))