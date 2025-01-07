def eelarve(kylalised):
    kylalised = int(input("mitu inimest on kutsutud: ? "))
    eelarve = kylalised * 10 + 55
    return eelarve

max_inimesed =int(input("mitu on kutsutud?"))
min_inimesed = int(input("mitu inimest tuleb?"))

print(eelarve(max_inimesed))
print(eelarve(min_inimesed))