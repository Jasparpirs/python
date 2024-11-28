#Jaspar 28.11.2024
#17

# kogu tehingute arvu
# positiivsete tehingute arvu
# positiivsete tehingute kogusumma

fail = open("pangakonto.txt")
tekstiread = (fail.readlines())
tehingute_arv = len(tekstiread)
pos_tehinguid = 0
pos_tehingute_summa = 0

for i in tekstiread:
    if float(i.strip()) > 0:
        pos_tehinguid += 1
        pos_tehingute_summa +=float(i)

print(f"Tehinguid kokku: {tehingute_arv}")
print(f"Pos tehinguid kokku: {pos_tehinguid}")
print(f"Tehingute summa: {pos_tehingute_summa}")



fail =  open("palgad.txt", encoding="utf8")
npalgad =[]
mpalgad =[]
read = fail.readlines()
for i in read:
    r = i.split(",")
    print(r[3])
    if r[3] == "Mees": 
        mpalgad.append(float(r[6]))
    else:
        npalgad.append(float(r[6]))
print(mpalgad)
print(npalgad)

print(sum(mpalgad)/len(mpalgad))
print(sum(npalgad) /len(npalgad))

import os
fail =  open("palgad.txt", encoding="utf8")
read = fail.readlines()
mpalgad = []
npalgad = []
 
os.mkdir("palgad1")
for i in read:
    r=i.split(",")
    failinimi = r[0] + "_" + r[1] +
     