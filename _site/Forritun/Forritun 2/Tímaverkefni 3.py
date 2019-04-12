# Einar Karl Pétursson
# 11/4/2019
import random


# Klasar:
class Jofnur:
    def jafna(tala1, tala2, tala3):
        l = []
        l.append(tala1)
        l.append(tala2)
        l.append(tala3)
        return max(l)


class Paskaegg:
    def __init__(self, t, s):
        self.tegund_eggs = t
        self.staerd = s

    def __str__(self):
        return "Ég er páskaegg af tegundinni "+str(self.tegund_eggs)+" og er af stærðinni "+str(self.staerd)+"."


# Def:
def bua_til_lista(byrjun, endir, fjoldi=100):
    l = []
    for x in range(fjoldi):
        x = random.randint(byrjun, endir)
        l.append(x)
    return l


def syna_lista(tolulisti):
    print(':'.join(map(str, tolulisti)))


def medaltal(tolulisti):
    summa = 0
    for x in tolulisti:
        summa = summa + x
    fjoldi = 0
    for i in tolulisti:
        fjoldi = fjoldi + 1
    medaltal = summa / fjoldi
    return round(medaltal, 3)


def deilanlegt(tolulisti, tala):
    l = []
    for x in tolulisti:
        if x % tala == 0:
            l.append(x)
    return l


def skila_bili(tolulisti, fra, til):
    l = []
    for x in tolulisti:
        if x in range(fra, til):
            l.append(x)
    return l




val = ""
while val != "0":
    print("0. Hætta \n1. Verkefni 1\n2. Verkefni 2")
    val = input("Veldu 1 2 eða 0 til að hætta ")
    if val == "1":
        listi1 = bua_til_lista(100, 200)
        syna_lista(listi1)
        print(medaltal(listi1))
        listi2 = bua_til_lista(1, 50, 50)
        print(deilanlegt(listi2, 3))
        print(skila_bili(listi2, 21, 30))
    elif val == "2":
        print("Hæsta talan er:", Jofnur.jafna(1, 5, 3))
        egg = "Nói siríus"
        staerd = 4
        print(Paskaegg(egg, staerd))
    elif val == "0":
        print("Ókei bæ")
    else:
        print("Rangur Innsláttur")