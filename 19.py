#jaspar
#07.01.25


import json

kl_12=0
kl_11=0
kl_10=0

with open('haridustulemused.json', 'r', encoding='utf-8') as file:
    opilased = json.load(file)

for opilane in opilased:
    if opilane['klass'] == '12':
        kl_12+=1
        print(opilane['nimi'])
        for tegevus in opilane['tegevused']:
            print(tegevus)
        print("---------------------")
    if opilane['klass'] == '11':
            kl_11+=1
    if opilane['klass'] == '10':
            kl_10+=1

print(f"12. klassis õpib {kl_12}")
print(f"11. klassis õpib {kl_11}")
print(f"10. klassis õpib {kl_10}")




