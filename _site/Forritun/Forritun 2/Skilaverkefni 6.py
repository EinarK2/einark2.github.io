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

    def fight(self):
        pass

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

print("FIGHT")

if herdeildA[0].afl < herdeildB[0].afl:
    # Þá vinnur A
    # Taka þarf eitt líf af B
    # B þarf að fara adtast í sinn lista ef hann á eftir líf
    # Ef B á engin líf eftir þarf að eyða honum úr listanum
    print("wowza")
a0 = herdeildA.pop(0)
print("Poppað tilvik", a0)
print(" HERDEILD A EFTIR POP")
tel = 1
for x in herdeildA:
    print("Hermaður", tel, x)
    tel += 1
print("HERDEILD A EFTIR INSERT")
# Bæta við stkainu sem tapaði aftast
herdeildA.append(a0)
tel = 1
for x in herdeildA:
    print("Hermaður", tel, x)
    tel += 1



