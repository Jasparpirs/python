#jaspar
#07.01.25

import json

with open('haridustulemused.json', 'r', encoding='utf-8') as file:
    opilased = json.load(file)

print(opilased[nimi])
# json_data = '{"name": "John Doe", "klass": 35, "city": "New York"}'
# klass = extract_key_value(json_data, "klass")
# print(klass) 