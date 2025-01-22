import json
import requests
sisesta_otsitav = input("Sisesta nimi: ")
#jaspar 22.01.2025

# API päringu tegemine
url = f"https://dummyjson.com/todos/{sisesta_otsitav}"
response = requests.get(url)

if response.status_code == 200:
    todos = response.json()
    print(f"Pealkiri: {todos['todo']}")
    print(f"Kasutaja ID: {todos['userId']}")
    print(f"ID: {todos['id']}")
    print(f"Kas tehtud: {todos['completed']}")
else:
    print("Ei leitud sellist ID-d")
   
    



