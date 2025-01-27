import requests
#jaspar pirs
#27.01.25

otsitav_s6na = input("Sisesta sona mida on vaja sul otsida: ")

url = "https://dummy-json.mock.beeceptor.com/todos"
response = requests.get(url)

if response.status_code == 200:
    todos = response.json()['title']
    olemas = False
    for todo in todos:
        if otsitav_s6na.lower() in todo['title,'].lower():
                olemas == True
                print(f"pealkiri: {todo['title']}")
                print(f"kasutaja id: {todo['userId']}")
                print(f"id: {todo['id']}")