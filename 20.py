#jaspar 14.01.25
import requests

import requests

# API võtme ja linna nime määramine
city = "HaapsAlu"
api_key = "f4718da5798ba9aea22497d29515b83a"
url = f"https://api.openweathermap.org/data/2.5/weather?q=HAapsalu&appid=f4718da5798ba9aea22497d29515b83a&units=metric"

# API päringu tegemine
response = requests.get(url)

# Vastuse kontrollimine
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Sisesta soovitud linn: {city}")
    print(f"Temperatuur: {temperature} °C")
else:
    print("Viga andmete allalaadimisel:", response.status_code)