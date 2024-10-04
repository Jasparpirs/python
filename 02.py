from math import *
#jaspar Pirs
# Harjutus 02
#30.09.24

#3.ümbermõõt
a,b,c = 1,2,3
P = a + b + c
print("Kolmnurga ümbermõõt on;",P)



#4.toote hind
# 7,35
toode = 36.75
soodushind = 0.4
kogus = 3
kokku = (toode - (toode * soodushind))*kogus
print("Kokku on")

#5.pitsa
pitsa = 12.90
jootraha = 1.29
kokku = 14.19
summa = (14.19 / 3)
print("summa on")



#6.rulluisutajad
kiirus = 29.9
aeg = 24/60
dist = kiirus * aeg
print("rulluisutaja jõuab:",dist,"km kaugusele")

#7.Hüpotenuus **
a,b = 16,9
c = sqrt(a**2+b**2)
print("hüpotenuus on:",c)

#8.ajateisenuds // %
aeg = 72
h = aeg//60
m = aeg % 60
print(h,":",m)

#9.arvutisüsteemid
arv = int(input("lisa arv: "))
Kahend = bin(arv)
kuust = hex(arv)
print("sinu teisendused on: ",kahend, "ja",kuust)

#10.kütusekulu

l = int(input("Lisa tangitud liitrid: "))
km = int(input("Lisa läbitud kilomeetrid: "))
kytusekulu = l/(km/100)
print("Sinu kütusekulu on",kytusekulu)
