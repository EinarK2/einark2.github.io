# Einar Karl Pétursson
# 4/4/2019 / 9/4/2019
import random


# Klasinn Hermann hefur eiginleikana líf, vopn og afl
class Hermann:
    def __init__(self, l, v, a):  # Skilgreini líf, vopn og afl með smiði
        self.lif = l
        self.vopn = v
        self.afl = a

    def __str__(self):
        vopn = ""
        if self.vopn == 1:  # geri if setningar til að skilgreina vopn sem ákveðið vopn
            vopn = "sverð"
        elif self.vopn == 2:
            vopn = "spjót"
        elif self.vopn == 3:
            vopn = "exi"
        return "hefur "+str(self.lif)+" líf. Vopnið er: "+vopn+". \tAflið er: "+str(self.afl)  # Skilar streng


def prentaHerdeildir(listi):  # Def sem prentar lista (herdeild)
    tel = 1
    for x in listi:
        print("Hermaður", tel, x)
        tel += 1


herdeildA = []  # Skilgreini tvo lista
herdeildB = []
for x in range(5):
    lif = random.randint(1, 5)
    vopn = random.randint(1, 3)
    afl = random.randint(1, 5)
    h1 = Hermann(lif, vopn, afl)
    herdeildA.append(h1)
for x in range(5):                  # Geri hermenn og set í lista
    lif = random.randint(1, 5)
    vopn = random.randint(1, 3)
    afl = random.randint(1, 5)
    h2 = Hermann(lif, vopn, afl)
    herdeildB.append(h2)
print("Herdeild A:")
prentaHerdeildir(herdeildA)
print("Herdeild B:")
prentaHerdeildir(herdeildB)
tel = 1  # Skilgreini teljara
flag = False  # Skilgreini flag
while flag != True:  # Keyrir á meðan flag er ekki True
    try:
        print("---- BARDAGI", tel, "----")  # Svo maður viti númer  hvaða bardaga maður er á
        # If setning ef A tapar á móti B
        if herdeildA[0].afl < herdeildB[0].afl:
            print("B vann A þar sem afl B var", herdeildB[0].afl, "en afl A var", herdeildA[0].afl)
            a0 = herdeildA.pop(0)  # Tek hermann úr herdeildA
            a0.lif = a0.lif - 1  # Tek líf af hermanninum
            if a0.lif == 0:  # Ef líf hanns er 0: (ekki settur í lista
                print("Hermaður A dó þar sem hann var bara með eitt líf eftir")
            else:  # annars: (Settur í lista)
                herdeildA.append(a0)  # Bæta við stakinu sem tapaði aftast

            print("HERDEILD A EFTIR BARDAGA:")
            prentaHerdeildir(herdeildA)
            print("HERDEILD B EFTIR BARDAGA:")
            prentaHerdeildir(herdeildB)
        # If setning ef B tapar á móti A
        elif herdeildA[0].afl > herdeildB[0].afl:
            print("A vann B þar sem afl A var", herdeildA[0].afl, "en afl B var", herdeildB[0].afl)
            b0 = herdeildB.pop(0)  # Mjög svipað gert hér
            b0.lif = b0.lif - 1
            if b0.lif == 0:
                print("Hermaður B dó þar sem hann var bara með eitt líf eftir")
            else:
                herdeildB.append(b0)
            print("HERDEILD A EFTIR BARDAGA:")
            prentaHerdeildir(herdeildA)
            print("HERDEILD B EFTIR BARDAGA:")
            prentaHerdeildir(herdeildB)
        # If setning ef Afl A og B er það sama
        elif herdeildA[0].afl == herdeildB[0].afl:
            print("Afl A og B er það sama!")
            # 1 Sverð  2 spjót  3 exi
            # Segjum að sverð vinnur exi, exi vinnur spjót og spjót vinnur sverð
            # If setningar fyrir vopnunum
            if herdeildA[0].vopn == 1 and herdeildB[0].vopn == 2:
                print("A (Sverð) tapar á móti B (spjót)")
                a0 = herdeildA.pop(0)  # Sami kóði og áðan
                a0.lif = a0.lif - 1
                if a0.lif == 0:
                    print("Hermaður A dó þar sem hann var bara með eitt líf eftir")
                else:
                    herdeildA.append(a0)

                print("HERDEILD A EFTIR BARDAGA:")
                prentaHerdeildir(herdeildA)
                print("HERDEILD B EFTIR BARDAGA:")
                prentaHerdeildir(herdeildB)

            elif herdeildA[0].vopn == 2 and herdeildB[0].vopn == 1:
                print("B (Sverð) tapar á móti A (Spjót)")
                b0 = herdeildB.pop(0)
                b0.lif = b0.lif - 1
                if b0.lif == 0:
                    print("Hermaður B dó þar sem hann var bara með eitt líf eftir")
                else:
                    herdeildB.append(b0)

                print("HERDEILD A EFTIR BARDAGA:")
                prentaHerdeildir(herdeildA)
                print("HERDEILD B EFTIR BARDAGA:")
                prentaHerdeildir(herdeildB)

            elif herdeildA[0].vopn == 3 and herdeildB[0].vopn == 2:
                print("B (Spjót) tapar á móti A (Exi)")
                b0 = herdeildB.pop(0)
                b0.lif = b0.lif - 1
                if b0.lif == 0:
                    print("Hermaður B dó þar sem hann var bara með eitt líf eftir")
                else:
                    herdeildB.append(b0)  # Bæta við stakinu sem tapaði aftast

                print("HERDEILD A EFTIR BARDAGA:")
                prentaHerdeildir(herdeildA)
                print("HERDEILD B EFTIR BARDAGA:")
                prentaHerdeildir(herdeildB)

            elif herdeildA[0].vopn == 2 and herdeildB[0].vopn == 3:
                print("A (Spjót) tapar á móti B (Exi)")
                print("A (Sverð) tapar á móti B (spjót)")
                a0 = herdeildA.pop(0)
                a0.lif = a0.lif - 1
                if a0.lif == 0:
                    print("Hermaður A dó þar sem hann var bara með eitt líf eftir")
                else:
                    herdeildA.append(a0)
                print("HERDEILD A EFTIR BARDAGA")
                prentaHerdeildir(herdeildA)
                print("HERDEILD B EFTIR BARDAGA:")
                prentaHerdeildir(herdeildB)

            # Ef ekkert af ofan virkar:
            else:
                print("Vopnin eru alveg eins svo þeir misstu báðir líf")
                a0 = herdeildA.pop(0)
                a0.lif = a0.lif - 1
                if a0.lif == 0:
                    print("Hermaður A dó þar sem hann var bara með eitt líf eftir")
                else:
                    herdeildA.append(a0)

                b0 = herdeildB.pop(0)
                b0.lif = b0.lif - 1
                if b0.lif == 0:
                    print("Hermaður B dó þar sem hann var bara með eitt líf eftir")
                else:
                    herdeildB.append(b0)

                print("HERDEILD A EFTIR BARDAGA")
                prentaHerdeildir(herdeildA)
                print("HERDEILD B EFTIR BARDAGA:")
                prentaHerdeildir(herdeildB)
        tel += 1  # Bæti við á teljarann eftir hverja lúppu
        if len(herdeildA) == 0:  # Ef fjöldi listans er 0:
                flag = True
                print("---- Leik lokið -----")
                print("Herdeild B vann!")
        elif len(herdeildB) == 0:
                flag = True
                print("---- Leik lokið -----")
                print("Herdeild A vann!")
    except:
        break  # Try og except er svo kóðinn krassi ekki
# og afsakið með allann þennann spagettí kóða
