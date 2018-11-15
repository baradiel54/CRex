import requests
from bs4 import BeautifulSoup

page = requests.get("https://statsroyale.com/tr/profile/2Q800RGQU/cards?sort=rarity")
soup = (BeautifulSoup(page.content, "html.parser"))
print(soup.prettify())
#a = [soup.find_all("div", class_="ui__tooltip ui__tooltipTop ui__tooltipMiddle cards__tooltip")[i].get_text() for i in
#     range(89)]
#print(a)

