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
    tel = 0
    for x in spil:
        if bunki[-1].tegund == spil[x - 1].tegund or bunki[-1].nr == spil[x - 1].nr:
            settuttolva = spil.pop(x - 1)
            bunki.insert(0, settuttolva)
            break
        else:
            tel += 1
            if tel == 4:
                print("Tölva gat ekki gert")
            else:
                spil.append(stokkur.pop(0))


tilvik = Spil(0, 0)
spilastokkur = tilvik.geraSpilaStokk()
synaspil(spilastokkur)

spilNotandi = []
spilTolva = []
kastbunki = []

for x in range(5):  # Tekur úr stokk
    spilNotandi.append(spilastokkur.pop(0))
    spilTolva.append(spilastokkur.pop(0))

# spilhendi(spilNotandi)  # Sýnir spil notanda

# spiltolvu(spilTolva)  # Sýnir spil tölvu

kastbunki.append(spilastokkur.pop(0))  # Tekur úr stokk

# spilbord(kastbunki)  # Sýnir borð

# ut = spilNotandi.pop(3)  # Tekur fjórða spil notanda 0 1 2 3
# kastbunki.insert(0, ut)  # setur spilið á borð

print("skrifa 'draga' til að draga")
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
            if kastbunki[-1].tegund == x.tegund or kastbunki[-1].nr == x.nr:
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
    elif ut == "pass":
        if dragatel != 4:
            print("Þú getur ekki gert pass")
        if dragatel == 4:
            print("þettaekkitilbúið")
            # Tölva gerir
    else:
        try:
            ut = int(ut)
            if kastbunki[-1].tegund == spilNotandi[ut-1].tegund or kastbunki[-1].nr == spilNotandi[ut-1].nr:
                settUt = spilNotandi.pop(ut-1)
                kastbunki.insert(0, settUt)
                # Tölva gerir
                tolvagerir(spilTolva, kastbunki, spilastokkur)
            else:
                print("Þú getur ekki sett út þetta spil")
        except:
            print("Þetta er ekki spil")



