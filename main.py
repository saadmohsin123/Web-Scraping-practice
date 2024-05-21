# import requests 
# from bs4 import BeautifulSoup as bs

# url = 'https://pk.khaadi.com/ready-to-wear/signature/kurta/'

# r = requests.get(url)
# r = r.text
# soup = bs(r, "lxml")
# price = soup.find("span",{"class" : "value cc-price"})
# description = soup.find("h2", {"class" : "pdp-link-heading"})
# print(price.string)
# print(description.string)

# import requests

import requests
from bs4 import BeautifulSoup as bs
import re

url = 'https://pk.khaadi.com/ready-to-wear/signature/kurta/?start=0&sz=164'
r = requests.get(url)

soup = bs(r.text, "lxml")
data = soup.find_all(string= re.compile("10,000"))
print(data)