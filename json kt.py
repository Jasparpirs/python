
import requests
#jaspar 22.01.2025

otsitav_sona = input("Sisesta sona mida on vaja sul otsida: ")
# API päringu tegemine
url = "https://dummyjson.com/todos"
response = requests.get(url)

if response.status_code == 200:
    todos = response.json()['todos']
    olemas = False
    for todo in todos:
        if otsitav_sona.lower() in todo['todo'].lower():
            print(f"Pealkiri: {todo['todo']}")
            print(f"Kasutaja ID: {todo['userId']}")
            print(f"ID: {todo['id']}")
            olemas = True
    if not olemas:
        print("Sellist asja ei leitud yles.")
else:
    print("Tekkis mingi probleem.")




