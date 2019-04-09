# Einar Karl Pétursson
# 4/4/2019
import random


class Hermann:
    def __init__(self, l, v, a):
        self.lif = l
        self.vopn = v
        self.afl = a

    def __str__(self):
        vopn = ""
        if self.vopn == 1:
            vopn = "sverð"
        elif self.vopn == 2:
            vopn = "spjót"
        elif self.vopn == 3:
            vopn = "exi"
        return "hefur "+str(self.lif)+" líf. Vopnið er: "+vopn+".\tAflið er: "+str(self.afl)

herdeildA = []
herdeildB = []
for x in range(5):
    lif = random.randint(1, 5)
    vopn =random.randint(1, 3)
    afl = random.randint(1, 5)
    h1 = Hermann(lif, vopn, afl)
    herdeildA.append(h1)
for x in range(5):
    lif = random.randint(1, 5)
    vopn =random.randint(1, 3)
    afl = random.randint(1, 5)
    h2 = Hermann(lif, vopn, afl)
    herdeildB.append(h2)
print("Herdeild A:")
tel = 1
for x in herdeildA:
    print("Hermaður", tel, x)
    tel += 1
print("Herdeild B:")
tel = 1
for x in herdeildB:
    print("Hermaður", tel, x)
    tel += 1

print("--- FIGHT ---")

flag = False
while flag != True:
    try:
        # If setning ef A tapar á móti B
        if herdeildA[0].afl < herdeildB[0].afl:
            print("B vann A þar sem afl B var", herdeildB[0].afl, "en afl A var", herdeildA[0].afl)
            a0 = herdeildA.pop(0)
            a0.lif = a0.lif - 1
            if a0.lif == 0:
                print("Hermaður A dó þar sem hann var bara með eitt líf eftir")
            else:
                herdeildA.append(a0)  # Bæta við stakinu sem tapaði aftast
            print("HERDEILD A EFTIR BARDAGA")
            tel = 1
            for x in herdeildA:
                print("Hermaður", tel, x)
                tel += 1

            if herdeildA == 0:
                flag = True
                print("Herdeild B vann!")
        elif herdeildA[0].afl > herdeildB[0].afl:
            print("A vann B þar sem afl A var", herdeildA[0].afl, "en afl B var", herdeildB[0].afl)
            b0 = herdeildB.pop(0)
            b0.lif = b0.lif - 1
            if b0.lif == 0:
                print("Hermaður B dó þar sem hann var bara með eitt líf eftir")
            else:
                herdeildB.append(b0)  # Bæta við stakinu sem tapaði aftast

            print("HERDEILD B EFTIR BARDAGA")
            tel = 1
            for x in herdeildB:
                print("Hermaður", tel, x)
                tel += 1

        elif herdeildA[0].afl == herdeildB[0].afl:
            print("Afl A og B er það sama!")
            # 1 Sverð  2 spjót  3 exi
            # Segjum að sverð vinnur exi, exi vinnur spjót og spjót vinnur sverð

            if herdeildA[0].vopn == 1 and herdeildB[0].vopn == 2:
                print("A (Sverð) tapar á móti B (spjót)")
                a0 = herdeildA.pop(0)
                a0.lif = a0.lif - 1
                if a0.lif == 0:
                    print("Hermaður A dó þar sem hann var bara með eitt líf eftir")
                else:
                    herdeildA.append(a0)  # Bæta við stakinu sem tapaði aftast

                print("HERDEILD A EFTIR BARDAGA")
                tel = 1
                for x in herdeildA:
                    print("Hermaður", tel, x)
                    tel += 1

            elif herdeildA[0].vopn == 2 and herdeildB[0].vopn == 1:
                print("B (Sverð) tapar á móti A (Spjót)")
                b0 = herdeildB.pop(0)
                b0.lif = b0.lif - 1
                if b0.lif == 0:
                    print("Hermaður B dó þar sem hann var bara með eitt líf eftir")
                else:
                    herdeildB.append(b0)  # Bæta við stakinu sem tapaði aftast

                print("HERDEILD B EFTIR BARDAGA")
                tel = 1
                for x in herdeildB:
                    print("Hermaður", tel, x)
                    tel += 1

            elif herdeildA[0].vopn == 3 and herdeildB[0].vopn == 2:
                print("B (Spjót) tapar á móti A (Exi)")
                b0 = herdeildB.pop(0)
                b0.lif = b0.lif - 1
                if b0.lif == 0:
                    print("Hermaður B dó þar sem hann var bara með eitt líf eftir")
                else:
                    herdeildB.append(b0)  # Bæta við stakinu sem tapaði aftast

                print("HERDEILD B EFTIR BARDAGA")
                tel = 1
                for x in herdeildB:
                    print("Hermaður", tel, x)
                    tel += 1

            elif herdeildA[0].vopn == 2 and herdeildB[0].vopn == 3:
                print("A (Spjót) tapar á móti B (Exi)")
                print("A (Sverð) tapar á móti B (spjót)")
                a0 = herdeildA.pop(0)
                a0.lif = a0.lif - 1
                if a0.lif == 0:
                    print("Hermaður A dó þar sem hann var bara með eitt líf eftir")
                else:
                    herdeildA.append(a0)  # Bæta við stakinu sem tapaði aftast
                print("HERDEILD A EFTIR BARDAGA")
                tel = 1
                for x in herdeildA:
                    print("Hermaður", tel, x)
                    tel += 1

            else:
                print("Vopnin eru alveg eins svo þeir misstu báðir líf")
                a0 = herdeildA.pop(0)
                a0.lif = a0.lif - 1
                if a0.lif == 0:
                    print("Hermaður A dó þar sem hann var bara með eitt líf eftir")
                else:
                    herdeildA.append(a0)  # Bæta við stakinu sem tapaði aftast

                b0 = herdeildB.pop(0)
                b0.lif = b0.lif - 1
                if b0.lif == 0:
                    print("Hermaður B dó þar sem hann var bara með eitt líf eftir")
                else:
                    herdeildB.append(b0)  # Bæta við stakinu sem tapaði aftast
    except:
        break

print("Leik lokið")
# Hermann.Atapar()  try = if.  except = else.
