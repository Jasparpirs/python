#16.10.2024 Jaspar
#ül 4
import turtle


#ringi pindala ja turtle
try:
    r = 10
    s = 3.14*r**2
    p = 2 * 3.14 * r
    print(f"Program väljastab konsoolis: Ringi pindala on {s: .2f}")
    turtle.circle(r*2, 360)
    turtle.done()
except:
    Print("sisestus vale!")


"""
#kingistute pakkimine
try:
    kast = 5
    kingitustearv = int(input("Lisa kingituste arv: "))
    komplektid = kingitustearv//kast #täisarvu jaoks //
    yle= kingitustearv%kast   #jäägi saamine
    Print(saad teha {komplektid} täis kinkekasti. Üle jääb {yle} kingitust)
except:
    print("lisasid koguse valesti")


#Faili allalaadimine
try:
    failisuurus = int(input("Sisesta faili suurus: "))
    downlkiirus = int(input("Sisesta Allalaadimise kiirus: "))
    aeg = failisuurus/downlkiirus
    print(f"Allalaadimiseks kulub {aeg} sekundit")
except:
    Print("Palun sisesta täisarvud!")
#raamatu allahindlus
ale = 0.3
hind = 12.5
kogus = int(input("Lisa raamatute kogus: "))
summa = (hind-(hind*ale))
print(f"{kogus} raamatu hind soodustega on {summa:0.2f}£. ")


#aia pikkus
a = int(input("Lisa 1 Külg: "))
b = int(input("Lisa 2 Külg: "))
p = 2*(a+b)
print(f"Aia kogupikkus on {p} meetrit.")
"""