#jaspar 05.12.24

ringide_arv = int(input("sisesta ringide arv!: "))
i = 1
koguarv = 0
while i <= ringide_arv:
    if i%2==0:
        koguarv +=i
        print(i)
        i+=1
        print(f"koguarv on: {koguarv}")
   
