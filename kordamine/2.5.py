import random
ounu = 14
poisse = 3
for i in range (poisse):
    print(random.randint(1,2))
    ounu -= random.randint(1,2)
    print(ounu)