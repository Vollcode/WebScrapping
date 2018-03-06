from bs4 import BeautifulSoup
from slugify import slugify
import requests
import json

'''
La documentacion puede ser encontrada en
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
'''

'''
LA MISION:
Rescatar la informacion basica sobre los estados miembro
de la Union Europea
'''

req  = requests.get("https://en.wikipedia.org/wiki/Member_state_of_the_European_Union")
data = req.text
soup = BeautifulSoup(data, "html.parser")
countries_collection = []
countries_html_table = soup.find_all("table", class_="wikitable")[0]
for tr in countries_html_table.find_all("tr"):
    td = tr.find_all("td")
    if not td:
        th = tr.find_all("th")
        header = [slugify(h.text) for h in th]
    else:
        country = dict()
        for i, h in enumerate(header):
            country[h] = td[i].text
        countries_collection.append(country)


print(json.dumps(countries_collection, indent=4, ensure_ascii=False, encoding="utf-8"))
