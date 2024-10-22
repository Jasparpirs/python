




laulud= "ALIKA – 'Bridges'",    "Anett x Fredi – 'Read Between The Lines'",    "villemdrillem – 'leekiv armastus'",    "Clicherik & Mäx – 'PAKSUD'",    "nublu – 'ära ärata'",    "NOËP – 'Move Your Feet'",    "Trad.Attack! – 'Bring It On'",   "Bedwetters – 'It Is What It Is'",  "Reket – 'Panama paberid'","Grete Paia – 'Võluväel'"

for i in range(10):
    print(str(i+1)+". "+laulud[i])

    try:
        valik =int(input("Vali lugu 1-10: "))
        print(f"mängin: {laulud[valik-1]}")
    except:
        print("Tegid vale otsuse :")
