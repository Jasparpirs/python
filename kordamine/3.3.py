#jaspar 05.12.24
import os
fail=open("konto.txt",encoding="UTF-8")



for rida in fail:
    if float(rida) >=0:
        print(rida)
