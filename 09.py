#24.10.24 Jaspar
#09
# import random




# # Genereeri ja kuva arvud arvud 1-20
# for i in range(1,21):
#     print(i, end=" ")
# print()
# # Genereeri ja kuva 20 suvalist arvu vahemikus 1-99
# for i in range(1,21):
#     print(random.randint(1, 100), end=" ")
# print()
# # Kasuta loendit 60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75
# # Leia paaris ja paaritud arvud ning lisa oma loendisse
# # Kuva paaris ja paritute arvude summad
# loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
# paaris = []
# paaritud = []
# for i in loend:
#     if i%2==0:
#         paaris.append(i)
#     else:
#             paaritud.append(i)
        

# print(f"Paaris arvude summa: {sum(paaris)}")
# print(f"Paaris arvude summa: {sum(paaritud)}")

# # Kuva arvud 1-42
# # Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
# # Arvud, mis jagunevad 5, lisa tekst TAK (näiteks 5 TAK)
# # Kui jagunevad mõlemaga, siis lisa tekst TIKTAK (näiteks 15 TIKTAK)
# for i in range(1,43):
#      if i%3==0 and  i%5==0:
#      print
     
#      print(i,TIK, end=" ")
#      elif i%5==0

# print(i,TAK, end=" ")


     
# # Kuva nimekirjast unikaalsed nimed:
# nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
# unikaalse_nimed = []
# for nimi in nimed:
#    if nimi not in unikaalse_nimed:
#     unikaalse_nimed.append(nimi)

# for nimi in unikaalse_nimed:
#     print(nimi)


# Sulle on saadetud õpilaste keskmised hinded, mille lisasid loendisse. Eralda hinded ning leia kogu rühma parim ja kehvem tulemus ning keskmine hinne.
# ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]
# hinded = []

# for i in ryhma_hinded:
#     print(f"parim tulemus{max(hinded)}")
# print(f"halvim {min(hinded)}")
# print(f"keskmine{sum(hinded)}")




# Koosta programm, mis genereerib ja kuvab korrutustabeli, kus iga number korrutatakse iseendaga:
# Näiteks:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4

# for i in range(11):
#     print(f"{i} x {i} = {i*i}")



import random






# Loo programm, mis loob suvalised tehted 1-100 arvudega.
# tehted = ['+','-','*','/']
# for _  in range(11):
#     i = random.randint(1,10)
#     j = random.randint(1,10)
#     tehe = random.choice(tehted)
#     if tehe=="+":
#         print(f"{i} {tehe} {j} = {i*j}")
#         vastus = int(input("vastus: "))
#         if vastus==i+j:
#             print("õige")
#             punktid+=1
        
#     elif tehe=="+":
#         print(f"{i} {tehe} {j} = {i*j}")
#     elif tehe=="+":
#         print(f"{i} {tehe} {j} = {i*j}")
#     else:
#         print(f"{i} {tehe} {j} = {round(i/j,2)}")


#Sama sugused kujundid





# Paariarvude summa
even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 3, 32, 34, 36, 38]
summa = 0

for i in even_nums:
     if i % 2 != 0:  
         break
     summa += i 

if summa > 0 and i % 2 != 0:  
    print(f"tsükkel lõpes paaritu arvu tõttu: {i}.")
else:
    print("tsükkel lõpes")
    print(f"paarisarvude summa on: {summa}.")


# Mitmemõõtmelise massiivi kasutamine for-tsükliga
ev_data = [
['vehicle', 'range', 'price'],
['Tesla Model Y Long Range', '330', '58990'],
['Volkswagen ID.4 Pro', '260', '39995'],
['Ford Mustang Mach-E', '300', '42995'],
['Audi e-tron GT', '238', '102700'],
['Nissan Leaf', '149', '27400'],
['BMW iX xDrive50', '324', '83995'],
['Polestar 2', '265', '45500'],
['Kia EV6 Long Range', '310', '47795'],
['Mercedes-Benz EQS 450+', '350', '102310'],
['Hyundai Kona Electric', '258', '37400']
]
