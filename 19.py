#jaspar
#07.01.25

import json

with open('haridustulemused.json', 'r', encoding='utf-8') as file:
    books = json.load(file)

for book in books:
    nimi = book['nimi']
    klass = book['klass']

klasside_arv = {10,11,12}

if klasside_arv > 11:
    print(klass)