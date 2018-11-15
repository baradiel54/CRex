import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


page = requests.get("https://statsroyale.com/tr/profile/2Q800RGQU/cards?sort=rarity")
soup = (BeautifulSoup(page.content, "html.parser"))
print(soup.prettify())

card_names = [i.get_text() for i in soup.find_all("div", class_="ui__tooltip ui__tooltipTop ui__tooltipMiddle cards__tooltip")]
print(card_names)

card_levels = []
for i in soup.find_all("span", class_="profileCards__level"):
    if i.get_text() != "":
        card_levels.append(int(re.sub("[^0-9]", "", i.get_text())))
    else:
        card_levels.append(0)
print(card_levels)

card_numbers = [int(i.get_text().split("/")[0]) for i in soup.find_all("div", class_="profileCards__meter__numbers")]
for i in range(len(card_levels)):
    if card_levels[i] == 0:
        card_numbers.insert(i, 0)
print(card_numbers)

df = pd.DataFrame({"Card Name": card_names, "Card Level": card_levels, "Card Numbers": card_numbers})
writer = pd.ExcelWriter("C:/Users/Arch/Desktop/Deneme2.xlsx", engine="xlsxwriter")
df.to_excel(writer, startrow=0, startcol=-1)
writer.save()