#Einar Karl P
#30.01.2019
import csv
import random
from random import shuffle
skra=open("text.csv",encoding="utf-8-sig")
lesari=csv.reader(skra,delimiter=";")
spurningar=list(lesari)
skra.close()
shuffle(spurningar)
rett=0
rangt=0
teljari=1
for i in spurningar:
    print("Spurning",teljari,":",i[0])
    svar=input("Sláðu inn svar: ")
    if svar==i[1]:
        print("Svarið er rétt")
        rett=rett+1
    elif svar !=i[1]:
        svar=input("Svarið er rangt, reyndu aftur: ")
        if svar == i[1]:
            print("Svarið er rétt")
            rett = rett + 1
        elif svar !=i[1]:
            print("Svarið er rangt")
            rangt=rangt+1
    teljari = teljari + 1
print("Rétt svör eru:",rett)
print("Röng svör eru:",rangt)

