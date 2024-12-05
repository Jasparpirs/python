#jaspar 05.12.2024

num_inimesed = int(input("Sisesta inimeste arv: "))
bussi_kohad = int(input("Sisesta bussi kohtade arv: "))

busside_arv = num_inimesed / bussi_kohad 
inimesed_viimases_bussis = num_inimesed % bussi_kohad

if inimesed_viimases_bussis > 0:
    busside_arv +1 
print(f"busse vaja: {busside_arv}")
print(f"inimesed viimases bussis: {inimesed_viimases_bussis}")