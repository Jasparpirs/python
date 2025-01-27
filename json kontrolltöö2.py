import requests
#jaspar pirs
#27.01.25

otsitav_s6na = input("Sisesta sona mida on vaja sul otsida: ")

url = "https://dummy-json.mock.beeceptor.com/todos"
response = requests.get(url)

if response.status_code == 200:
    todos = response.json()
    for todo in todos:
        if otsitav_s6na in todo['title']:
                print(f"pealkiri: {todo['title']}")
    else:
        print("ei leitud")