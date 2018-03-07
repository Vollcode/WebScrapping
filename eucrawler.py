'''	-- Flujo Basico WS --

	1. Seleccionar el Contenido
	2. Obtener la URL inicial
	3. Obtener el HTML de la URL
	4. Parsear el texto del HTML
	5. Seleccionar datos
	6. Procesar los datos
	7. (Repetir 3 si hay mas URL)'''




# BeautifulSoup 4 es una libreria para extraer datos de HTML y XML
from bs4 import BeautifulSoup

# slugify se encarga de parsear el encoding de los caracteres en UNICODE
from slugify import slugify

# libreria para realizar HTTP requests
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

# Lanzamos la request al endpoint del que queremos obtener informacion
req  = requests.get("https://en.wikipedia.org/wiki/Member_state_of_the_European_Union")
# con text accedemos al objeto que nos devuelve la respuesta
data = req.text
# Declaramos la acción que deseamos realizar con BS4
soup = BeautifulSoup(data, "html.parser")

countries_collection = []

# Establecemos que elementos de HTML deseamos scrappear
countries_html_table = soup.find_all("table", class_="wikitable")[0]
# Por cada row de la tabla
for tr in countries_html_table.find_all("tr"):
	# Buscamos el data que hay en cada una
    td = tr.find_all("td")
    if not td:
        th = tr.find_all("th")
        header = [slugify(h.text) for h in th]
    else:
		# Crea un diccionario clave-valor y pone la información de las th como clave y las td como valor
        country = dict()
        for i, h in enumerate(header):
            country[h] = td[i].text
        countries_collection.append(country)

# Print del resultado
print(json.dumps(countries_collection, indent=4, ensure_ascii=False, encoding="utf-8"))
