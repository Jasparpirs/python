#Jaspar
# 07.01.25
import csv


faili_nimi = 'EstonianBasketballGames.csv'
Meeskonnad= {}

with open(faili_nimi, mode='r', encoding='utf-8') as fail:
   
    dict_reader = csv.DictReader(fail)
   
    for rida in dict_reader:
        mk= rida['Team 1']
        mk2= rida['Team 2']
        if mk not in Meeskonnad:
            Meeskonnad[mk] = 0
        if mk2 not in Meeskonnad:
            Meeskonnad[mk] = 0

        if mk in Meeskonnad:
            Meeskonnad[mk] +=1
        if mk2 in Meeskonnad:
            Meeskonnad[mk2] +=1    




print(f"osales {len(Meeskonnad)} Meeskonda")



faili_nimi = 'Meeskonnad.csv'



# Ava fail kirjutamiseks UTF-8 kodeeringus, lisades BOM-i, ja kasuta semikoolonit veerueraldajana
with open(faili_nimi, 'w', encoding='utf-8') as fail:
    csv_fail = csv.writer(fail, delimiter=';', lineterminator='\n')  # Semikoolon veerueraldajana
    for key, value in Meeskonnad.items():
        csv_fail.writerow([key, value])