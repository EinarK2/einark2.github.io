# Einar Karl Pétursson
# 4/30/2019 - ?
# Olsen Olsen
import random


class Spil:
    def __init__(self, t, n):
        self.tegund = t
        self.nr = n

    def __str__(self):
        tegund = ""
        nr = ""
        if self.tegund == 1:
            tegund = "♥"
        elif self.tegund == 2:
            tegund = "♠"
        elif self.tegund == 3:
            tegund = "♦"
        elif self.tegund == 4:
            tegund = "♣"
        if self.nr == 11:
            nr = "Gosi"
        elif self.nr == 12:
            nr = "Drottning"
        elif self.nr == 13:
            nr = "Kóngur"
        elif self.nr == 1:
            nr = "Ás"
        else:
            nr = str(self.nr)
        return tegund+" "+nr

    def geraSpilaStokk(self):
        l = []
        for t in range(1, 5):
            for n in range(1, 14):
                sl = Spil(t, n)
                l.append(sl)
        random.shuffle(l)
        return l


def synaspil(l):
    for x in l:
        print(x)


def spilbord(l):
    print("-" * 10, "BORÐ", "-" * 11)
    print(l[0])


def spilhendi(l):
    print("-" * 10, "HENDI", "-" * 10)
    for tel, x in enumerate(l):
        if tel != len(l)-1:
            print(x, end=" | ")
        else:
            print(x)


def spiltolvu(l):
    print("-"*10, "TÖLVA", "-"*10)
    for tel, x in enumerate(l):
        if tel != len(l) - 1:
            print(x, end="  |  ")
        else:
            print(x)


def tolvagerir(spil, bunki, stokkur):
    gert = False
    tel = 0
    for x in spil:
        if x.tegund == bunki[0].tegund or x.nr == bunki[0].nr:
            sett = spil.pop(spil.index(x))
            bunki.insert(0, sett)
            gert = True
            print("Tölva setti út", sett)
            break
    if gert == False:
        spil.append(stokkur.pop(0))
        if spil[-1].nr == bunki[0].tegund or spil[-1].tegund == bunki[0].tegund:
            sett = spil.pop(-1)
            bunki.insert(0, sett)
            print("Tölva dróg einu sinni")
            print("Tölva setti út", sett)
        else:
            spil.append(stokkur.pop(0))
            if spil[-1].nr == bunki[0].tegund or spil[-1].tegund == bunki[0].tegund:
                sett = spil.pop(-1)
                bunki.insert(0, sett)
                print("Tölva dróg tvisvar")
                print("Tölva setti út", sett)
            else:
                spil.append(stokkur.pop(0))
                if spil[-1].nr == bunki[0].tegund or spil[-1].tegund == bunki[0].tegund:
                    sett = spil.pop(-1)
                    bunki.insert(0, sett)
                    print("Tölva dróg þrisvar")
                    print("Tölva setti út", sett)
                else:
                    print("Tölva dróg þrisvar og gat ekki gert")




tilvik = Spil(0, 0)
spilastokkur = tilvik.geraSpilaStokk()
synaspil(spilastokkur)

spilNotandi = []
spilTolva = []
kastbunki = []

for x in range(5):  # Tekur úr stokk
    spilNotandi.append(spilastokkur.pop(0))
    spilTolva.append(spilastokkur.pop(0))

kastbunki.append(spilastokkur.pop(0))  # Tekur úr stokk

# spilbord(kastbunki)  # Sýnir borð

# ut = spilNotandi.pop(3)  # Tekur fjórða spil notanda 0 1 2 3
# kastbunki.insert(0, ut)  # setur spilið á borð

print("\nLeiðbeiningr:\nskrifa 'draga' til að draga")
dragatel = 0
on = True
draga = True
while on:
    print()
    spiltolvu(spilTolva)  # Sýnir spil tölvu
    spilhendi(spilNotandi)  # Sýnir spil notanda
    spilbord(kastbunki)  # Sýnir borð
    print()
    ut = input("Hvaða spil viltu setja út? ")
    if ut == "draga":
        for x in spilNotandi:
            if kastbunki[0].tegund == x.tegund or kastbunki[0].nr == x.nr:
                print("Þú mátt ekki draga")
                draga = False
                break
            else:
                draga = True
        if draga == True:
            dragatel += 1
            if dragatel == 4:
                print("Þú mátt ekki draga meir gerðu pass")
            else:
                spilNotandi.append(spilastokkur.pop(0))
                print("\nÞú drógst", spilNotandi[-1])
    elif ut == "pass":
        if dragatel < 3:
            print("Þú getur ekki gert pass")
        if dragatel == 4 or dragatel == 3:
            # print("\n")
            dragatel = 0
            tolvagerir(spilTolva, kastbunki, spilastokkur)
            # Tölva gerir

    elif ut == "olsen":
        pass
    elif ut == "olsen olsen":
        pass

    else:
        try:
            ut = int(ut)
            if kastbunki[0].tegund == spilNotandi[ut-1].tegund or kastbunki[0].nr == spilNotandi[ut-1].nr:
                print("\nÞú settir út", spilNotandi[ut - 1])
                settUt = spilNotandi.pop(ut-1)
                kastbunki.insert(0, settUt)
                if len(spilNotandi) == 0:
                    print("Til hamingju þú vannst, takk fyrir að spila")
                    on = False
                else:
                    # Tölva gerir
                    dragatel = 0
                    tolvagerir(spilTolva, kastbunki, spilastokkur)
            else:
                print("Þú getur ekki sett út þetta spil")
        except:
            print("Þetta er ekki þekkt skipun")

    if len(spilTolva) == 0:
        print("Tölva vann, takk fyrir að spila")
        on = False


