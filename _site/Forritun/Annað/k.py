# Import:
import random
import math
# Föll:
def veldi(grunntala, veldistala):
    print(grunntala, "í", veldistala, "veldi er:", math.pow(grunntala, veldistala))
def nafnogkyn(nafn, kyn):
    if kyn == "kk":
        print("Sæll og blessaður", nafn)
    elif kyn == "kvk":
        print("Sæl og blessuð", nafn)
# Tuple:
herraTuple = ("Jón", "Ingi", "Arnar", "Halli", "Gunnar", "Gústi")
domuTuple = ("Jónína", "Inga", "Arna", "Halla", "Gunna", "Gústa")
#Dict:
stafrofsDict = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
# Valmynd:
val = " "
while val != "0":
    print("1. Skæri, blað, steinn")
    print("4. Byggingaupplýsingar")
    print("7. Danskeppnin")
    print("10. Stafrófið")
    print("13. Veldi")
    print("16. Kyn")
    print("0. Hætta")
    val = input("Veldu lið eða 0 til að hætta ")
    if val == "1":
        vinningar = 0
        tap = 0
        jafntefli = 0       # Skilgreini fjölda á mörgum hlutum
        fjoldiLeikja = 0
        val2 = 0
        nafn = input("Hvað heitiru fullu nafni? ")   # bið um nafn og aldur
        aldur = input("Hver er aldur þinn? ")
        while val2 != 4:  # Keyrir á meðan 4 er ekki valið
            print("1. fyrir skæri")
            print("2. fyrir blað")
            print("3. fyrir stein")
            print("4. fyrir að hætta")
            val2 = int(input("Veldu : "))
            cpu = random.randint(1, 3)  # CPU velur 1 2 eða 3
            if val2 == cpu:  # Skrifar jafntefli ef val er sama og CPU
                print("Jafntefli!")
                jafntefli += 1  # Bætir við á teljarann jafntefli
            elif val2 == 1:   # Ef valið var 1:
                if cpu == 3:  # Ef CPU valdi 3:
                    print("Steinn! Þú tapar!")
                    tap += 1  # Bætir við teljarann jafntefli
                else:
                    print("Blað! Þú vinnur!")  # Vinnur ef CPU valdi 2 í rauninni
                    vinningar += 1
            elif val2 == 2:  # Sama og áðan kemur næst bara fyrir aðar tölur
                if cpu == 1:
                    print("Skæri! Þú tapar")
                    tap += 1
                else:
                    print("Steinn! Þú vinnur")
                    vinningar += 1
            elif val2 == 3:
                if cpu == 2:
                    print("Blað! Þú tapar!")
                    tap += 1
                else:
                    print("Skæri! Þú vinnur")
                    vinningar += 1
            elif val2 == 4:  # Hér kemur þetta ef valið var 4
                print("Leik lokið")
            else:  # Þetta kemur ef skrifað var annað en 1 2 3 eða 4
                print("Rangur Innsláttur")
            fjoldiLeikja += 1 # Bætir við á teljarann fjoldi leikja í hvert sinn sem keyrt er
        print("Notandi Vann:\t Tölva vann:\t Jafntefli")  # Geri \t til að aðskilja orðin
        print(vinningar, "\t \t \t \t", tap, "\t \t \t \t", jafntefli)  # Geri 4 \t því þá aðskiljast tölurnar nóg
        print("Leikurinn var spilaður", fjoldiLeikja, "sinnum")  # Segir hve oft spilað var
        print("Nafn:", nafn)   # Skrifar nafn og aldur
        print("Aldur:", aldur)
    elif val == "4":
        heimilisfang = []
        arkitekt = []    # Skilgreini 3 lista
        byggingarAr = []
        teljari=1  # Skilgreini lista
        oft = int(input("Hversu margar byggingar viltu skrá? "))
        for x in range(oft):  # Keyrir eins oft og beðið var um
            print("Bygging", str(teljari)+":")  # Prentar bygging 1, 2 ,3 osfrv
            heimilisfang.append(input("Heimilisfang byggingar: "))  # Biður um heimilisfang og setur það í lista
            arkitekt.append(input("Arkitekt/hönnuður byggingar: "))  # Sama
            byggingarAr.append(input("Byggingarár: "))  # Sama
            teljari += 1  # Bætir við einn á teljarann
        print("Allar bygingar:")
        print("Staðsetning \t Arkitekt/Hönnuður \t Byggingarár")  # \t er til að aðskilja (tab)
        for x in range(oft):
            print(heimilisfang[x], "\t", arkitekt[x], " \t ", byggingarAr[x])  # Prentar x úr listunum með tab
    elif val == "7":
        print("Herra tuple er:")
        for x in herraTuple:   # Fer í gegnum tuple
            print(x, end=" ")  # og prentar innihaldið(x) með bili á milli
        print("Dömu tuple er:")
        for x in domuTuple:    # Fer í gegnum tuple
            print(x, end=" ")  # og prentar innihaldið(x) með bili á milli
        print("Pöruð saman í röð:")
        teljari=1 # geri teljari
        for x in range(len(herraTuple)):  # Keyrir í gegnum tuple eins og oft og len af því er
            print("Par", teljari, "er: \t", herraTuple[x], "og", domuTuple[x])  # Prentar innihöld í hvert sinn
            teljari += 1  # bætir við á teljarann
        print("Pöruð saman af handahófi:")
        teljari2=1 # annar teljari
        for x in range(len(herraTuple)):  # Keyrir í gegnum tuple eins og oft og len af því er
            print("Par", teljari2, "er: \t", random.choice(herraTuple), "og", random.choice(domuTuple))  # Prentar random úr tuple-in saman
            teljari2 += 1  # bætir við á teljarann
        stafur = input("Sláðu inn staf: ")
        listi = []  # Skilgreini lista
        for x in herraTuple:     # Fer í gegnum tup
            if x.count(stafur):  # Ef stafur er í tup
                listi.append(x)  # Setur x í listan
        for x in domuTuple:      # Sama hér:
            if x.count(stafur):
                listi.append(x)
        print("Hér eru nöfn með stafnum", stafur+":")
        for x in listi:
            print(x, end=" ")
        print()
        stafur = stafur.upper()  # Geri stafinn stóran
        listi2 = []  # Skilgreinir lista
        for x in herraTuple:  # Fer í gegnum tup
            if x[0] == stafur:  # Ef fyrsti stafurinn er sami og stafur:
                listi2.append(x)  # Setur x í listann
        for x in domuTuple:  # Sama hér:
            if x[0] == stafur:
                listi2.append(x)
        print("Hér eru nöfn sem byrja á stafnum", stafur+":")
        for x in listi2:
            print(x, end=" ")
        print()
        listi3 = []  # Skilgreinir lista
        for x in herraTuple:      # Fer í gegnum tup1
            if x.count("n") > 1:  # ef stafurinn 'n' er :
                listi3.append(x)  # Setur x í lista
        for x in domuTuple:  # Sama nema í tup2 en setur í sama lista
            if x.count("n") > 1:
                listi3.append(x)
        print("Nöfn sem eru með meira en eitt n:")
        for x in listi3:
            print(x, end=" ")
        print()
    elif val == "10":
        nafn = input("Sláðu inn nafn ")  # Biður um nafn
        listi = []  # Skilgreini lista
        for x in nafn:  # Keyrir í gegnum nafn
            if x in stafrofsDict:  # Ef x er í stafrófinu
                print(stafrofsDict[x], end=" ")  # Prentar tölurnar sem tengjast stöfunum
                listi.append(stafrofsDict[x])  # Setur tölurnar í lista
        print()  # Gerir bil
        print(nafn, "gefur summuna", sum(listi))  # Sýnir summu talnanna
        nafn2 = input("Sláðu inn nafn 2 ") # annað nafn
        listi2 = []  # skilgreinir annan lista
        for x in nafn2:  # Sama og áðan nema með nafn 2
            if x in stafrofsDict:
                listi2.append(stafrofsDict[x])
        if nafn > nafn2:  # Ef nafn 1 er lægri en nafn 2:
            print(nafn, "er með lægri summu en", nafn2)
        elif nafn < nafn2: # Ef nafn 1 er hærri en nafn 2:
            print(nafn, "er með hærri summu en", nafn2)
    elif val == "13":
        grunntala = int(input("Sláðu inn grunntölu: "))
        veldistala = int(input("Sláðu inn veldistölu: "))
        veldi(grunntala, veldistala)
    elif val == "16":
        nafn = input("Hvert er nafn þitt? ")
        kyn = input("Hvert er kyn þitt? (kk/kvk) ")
        nafnogkyn(nafn, kyn)
    elif val == "0":
        print("Takk fyrir að nota forritið mitt")
    else:
        print("Rangur Innsláttur")
