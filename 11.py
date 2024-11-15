#JASPAR 15.11.24
import turtle
import random


# Kilpkonn – kirjutada programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu. Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
# Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? Suvaline
# Mitu kujundit soovid joonistada? 5
# [Joonistab 5 kujundit, igaüks juhuslikult valitud tüübiga suvalistesse kohtadesse]
# Pärast joonistamist peaks programm pakkuma võimalust sisestada uued väärtused või väljuda programmist, jättes sisendi tühjaks.


print("-------------------- Joonistame kujundeid ------------------------")
print("Vali kujund: \n1 viisnurk, \n2 ring, \n3 ruut, \n4 suvaline")
kujund = int(input("Sisesta number: "))
arv = int(input("Mitu kujundit tahad(1-100): "))


def viisnurk():
    pass

def ring():
    pass

def suvaline ():
    pass

def ruut(a):
    for i in range(a):
        turtle.speed(0)
        turtle.penup()
        turtle.goto(random.randint(-400,400),random.randint(-400,400))
        turtle.pendown()
        for i in range(4):
            turtle.fd(100)
            turtle.lt(90)
    print("Valisid ruudu")
 
if kujund == 1:
    viisnurk()
elif kujund ==2:
    ring()
elif kujund == 3:
    ruut()
else:
    suvaline()






























def tervita(a):
    print("tere maailm"+a)

tervita("Jaspar")


#Kirjuta funktsioon pikim_sona(), mis võtab sisendiks sõnade listi ja tagastab pikima sõna pikkuse. Prindi tulemus konsooliaknasse.

def pikim_sona():
    pikimSona = 0
    for sona in sonad:
        if len(sona)>pikimSona:
            print(pikimSona)

sonad = ["üks", "kaks", "kolm, sadakuuskümmend"]

pikim_sona(sonad)

#Kirjuta funktsioon nimega kolm_pikimat_sona(), mis analüüsib sõnade listi ja leiab kolm kõige pikemat sõna. Lisa kontroll juhuks, kui sõnade arv pole piisav.

def kolm_pikimat_sona():
    uusSonastik = {}
    #uusSonastik["üks"]
    for sona in a:
        uusSonastik[sona] = len(sona)
    jar = sorted(uusSonastik.items(), key=lambda x:x[1], reverse=True)
    for i in range(3):
        print(jar[i][0])

#Kirjuta funktsioon, mis kontrollib, kas kahest sõnast koosnev sõne algab sama tähega.
#print(sarnased_esitahed('Vapper Vares')) # peaks tagastama True
#print(sarnased_esitahed('Lahe Känguru')) # peaks tagastama False

def sarnased_esitahed(a):
    tykk = a.split(" ")
    if tykk[0][0]==tykk[1][0]:
        return "True"
    else:
        return "False"

print(sarnased_esitahed("Vapper Vares"))
print(sarnased_esitahed("Lahe känguru"))


