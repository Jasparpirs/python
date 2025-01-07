#jaspar 05.12.24

taisarv=10
nisutera=0
if taisarv > 64:
    print("nii palju ruute ei ole")

if taisarv >= 1:
    nisutera+=1
    taisarv = 1

while taisarv >= 1:
    nisutera *=2
    korda -=1