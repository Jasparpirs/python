#Jaspar 20.11.2024
#ÜL 16

import os
import datetime


# operatsioonisüsteemi nimi
print(os.name)
# kasutaja nimi
print(os.getlogin())

print(os.getcwd())
try:
    mitu = 3
    for i in range (mitu):
     y = x.strftime("%d%m%Y")
    os.mkdir(y+"_"+str(i+1))
except:
   print("kataloogid juba olemas")

   items = os.listdir()
   for item in items:
      if os.path.isdir(item):
         print(item)

valik = input("lisa kataloogi nimi kustutamiseks: ")
try:
    os.rmdir(valik)
except:
   print("sellist kataloogi ei saa kustutada!")

items=os.listdir()
for item in items:
   if os.path.isdir(item):
      print(item)
      

print(os.listdir)
