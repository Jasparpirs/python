#jaspar 05.12.2024

fail = open("rebased.txt", encoding="UTF-8")

vastuvoetud = []
for rida in fail:
    vastuvoetud.append(int(rida))
print(vastuvoetud)
fail.close()