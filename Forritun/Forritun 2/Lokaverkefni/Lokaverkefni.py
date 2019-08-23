# Einar Karl Pétursson
# 4/30/2019 - ?
# Olsen Olsen
import random


# Klasinn spil hefur eiginleikana tegund og nr
class Spil:
    def __init__(self, t, n):  # Skilgreini tegund og nr með smiði
        self.tegund = t
        self.nr = n

    def __str__(self):
        tegund = ""
        nr = ""
        if self.tegund == 1:
            tegund = "♥"
        elif self.tegund == 2:  # geri if setningar til að hafa tegund sem merki
            tegund = "♠"
        elif self.tegund == 3:
            tegund = "♦"
        elif self.tegund == 4:
            tegund = "♣"
        if self.nr == 11:       # eða númer sem gosi eða drottning osfrv
            nr = "Gosi"
        elif self.nr == 12:
            nr = "Drottning"
        elif self.nr == 13:
            nr = "Kóngur"
        elif self.nr == 1:
            nr = "Ás"
        else:
            nr = str(self.nr)  # Svo númer eru strengir
        return tegund+" "+nr  # Skilar tegund og númer

    def geraSpilaStokk(self): # Til að gera spila stokk
        l = []
        for t in range(1, 5):
            for n in range(1, 14):  # For lúppurnar gera 13 spil fyrir hverja tegund (52 samtals)
                sl = Spil(t, n)
                l.append(sl)
        random.shuffle(l)  # Stokkar spilunum
        return l  # Skilar listanum


def synaspil(l):  # Til að sýna spil en svo notaði ég þetta ekkert
    for x in l:
        print(x)


def spilbord(l):
    print("-" * 15, "BORÐ", "-" * 16)  # Prentar x mörg strik, til að aðskilja
    print("\t"*4, l[0])  # Setti 4 \t því það lýtur vel út


def spilhendi(l):
    print("-" * 15, "HENDI", "-" * 15)  # sama
    for tel, x in enumerate(l):  # fer í gegnum lista og sér til um að endað er ekki á |
        if tel != len(l)-1:
            print(x, end=" | ")
        else:
            print(x)


def spiltolvu(l):
    print("-"*15, "TÖLVA", "-"*15)  # sama
    for tel, x in enumerate(l):  # sama
        if tel != len(l) - 1:
            print("X", end="  |  ")  # aðeins lengra hér
        else:
            print("X")  # Nota streng til að fela hvað tölva er með


def tolvagerir(spil, bunki, stokkur):
    gert = False  # Skilgreini þetta til að vita hvort tölva gat gert
    for x in spil:  # Fer í gegnum spil
        if x.nr == 8:  # Gáir hvort eih spil er 8
            randtegund = random.randint(1, 4)  # Tekur random tölu fyrir tegund
            if randtegund == 1:
                print("Tölva setti út", x, "og breytti í Hjarta")
                x.tegund = 1  # Breytir tegund í 1 (Hjarta)
                sett = spil.pop(spil.index(x))  # tekur spil úr hendi
                bunki.insert(0, sett)  # setur spil í bunka
                gert = True  # Staðfestir að það var gert
                break
            elif randtegund == 2:
                print("Tölva setti út", x, "og breytti í Spaða")
                x.tegund = 2
                sett = spil.pop(spil.index(x))  # sama
                bunki.insert(0, sett)
                gert = True
                break
            elif randtegund == 3:
                print("Tölva setti út", x, "og breytti í Tígul")
                x.tegund = 3
                sett = spil.pop(spil.index(x))  # sama
                bunki.insert(0, sett)
                gert = True
                break
            elif randtegund == 4:
                print("Tölva setti út", x, "og breytti í Lauf")
                x.tegund = 4
                sett = spil.pop(spil.index(x))  # sama
                bunki.insert(0, sett)
                gert = True
                break
        elif x.tegund == bunki[0].tegund or x.nr == bunki[0].nr:
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
                    print("Tölva dróg þrisvar og sagði pass")


tilvik = Spil(0, 0)
spilastokkur = tilvik.geraSpilaStokk()
# synaspil(spilastokkur)

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

print("\nLeiðbeiningar:\n\nSkrifaðu 'draga' til að draga og 'pass' ef þú getur ekki dregið meir")
print("\nSkrifaðu 'olsen' þegar þú ert með 2 spil eftir og getur sett eitt")
print("og 'olsen olsen' þegar þú ert með 1 spil eftir og getur sett það")
print("\nEf þú færð 8 geturu alltaf sett hana og þá geturu breytt um tegund spils")
print("\nTil að velja spil þarf að slá inn tölu eftir röð spilanna (1,2,3,4...)")
dragatel = 0
on = True
draga = True
olsen = False
olsenolsen = False
while on:
    print()
    spiltolvu(spilTolva)  # Sýnir spil tölvu
    spilhendi(spilNotandi)  # Sýnir spil notanda
    spilbord(kastbunki)  # Sýnir borð
    print()
    ut = input("Hvaða spil viltu setja? Þú getur líka gert draga, pass, olsen, olsen olsen : ")
    if ut == "draga":
        for x in spilNotandi:
            if x.nr == 8:
                print("\nÞú mátt ekki draga (Þú getur sett 8)")
                draga = False
                break
            elif kastbunki[0].tegund == x.tegund or kastbunki[0].nr == x.nr:
                print("\nÞú mátt ekki draga")
                draga = False
                break
            else:
                draga = True
        if draga == True:
            dragatel += 1
            if dragatel == 4:
                print("\nÞú mátt ekki draga meir gerðu pass")
            else:
                spilNotandi.append(spilastokkur.pop(0))
                print("\nÞú drógst", spilNotandi[-1])
    elif ut == "pass":
        for x in spilNotandi:
            if x.nr == 8:
                print("\nÞú mátt ekki gera pass (Þú getur sett 8)")
                break
        if dragatel < 3:
            print("\nÞú getur ekki gert pass")
        if dragatel == 4 or dragatel == 3:
            print("\nÞú gerðir pass")
            dragatel = 0
            tolvagerir(spilTolva, kastbunki, spilastokkur)
            # Tölva gerir

    elif ut == "olsen":
        if len(spilNotandi) == 2:
            print("\nVel gert, settu nú spilið")
            olsen = True
        else:
            print("\nÞú mátt ekki segja olsen")
    elif ut == "olsen olsen":
        if len(spilNotandi) == 1:
            print("\nVel gert, settu nú spilið")
            olsenolsen = True
        else:
            print("\nÞú mátt ekki segja olsen olsen")

    else:
        try:
            ut = int(ut)
            if spilNotandi[ut-1].nr == 8:
                print("\nÞú settir út", spilNotandi[ut - 1])
                flag = True
                while flag:
                    breyta = input("Fyrst spilið er 8 hvað viltu breyta spilinu í? (hjarta/spaði/tígull/lauf): ")
                    if breyta == "hjarta":
                        spilNotandi[ut-1].tegund = 1
                        spilNotandi[ut - 1].nr = 8
                        settUt = spilNotandi.pop(ut - 1)
                        kastbunki.insert(0, settUt)
                        flag = False
                    elif breyta == "spaði":
                        spilNotandi[ut - 1].tegund = 2
                        spilNotandi[ut - 1].nr = 8
                        settUt = spilNotandi.pop(ut - 1)
                        kastbunki.insert(0, settUt)
                        flag = False
                    elif breyta == "tígull":
                        spilNotandi[ut - 1].tegund = 3
                        spilNotandi[ut - 1].nr = 8
                        settUt = spilNotandi.pop(ut - 1)
                        kastbunki.insert(0, settUt)
                        flag = False
                    elif breyta == "lauf":
                        spilNotandi[ut - 1].tegund = 4
                        spilNotandi[ut - 1].nr = 8
                        settUt = spilNotandi.pop(ut - 1)
                        kastbunki.insert(0, settUt)
                        flag = False
                    else:
                        print("Rangur Innsláttur")
                        flag = True
                if len(spilNotandi) == 0:
                    print("Til hamingju þú vannst, takk fyrir að spila")
                    on = False
                else:
                    # Tölva gerir
                    dragatel = 0
                    tolvagerir(spilTolva, kastbunki, spilastokkur)
            elif kastbunki[0].tegund == spilNotandi[ut-1].tegund or kastbunki[0].nr == spilNotandi[ut-1].nr:
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

    if olsen == False and len(spilNotandi) == 1:
        print("\nÞú gleymdir að segja olsen svo þú færð 3 spil")
        spilNotandi.append(spilastokkur.pop(0))
        print("Þú drógst", spilNotandi[-1])
        spilNotandi.append(spilastokkur.pop(0))
        print("Þú drógst", spilNotandi[-1])
        spilNotandi.append(spilastokkur.pop(0))
        print("Þú drógst", spilNotandi[-1])

    if olsenolsen == False and len(spilNotandi) == 0:
        print("\nÞú gleymdir að segja olsen olsen svo þú færð 3 spil")
        spilNotandi.append(spilastokkur.pop(0))
        print("Þú drógst", spilNotandi[-1])
        spilNotandi.append(spilastokkur.pop(0))
        print("Þú drógst", spilNotandi[-1])
        spilNotandi.append(spilastokkur.pop(0))
        print("Þú drógst", spilNotandi[-1])

    if len(spilTolva) == 0:
        print("Tölva vann, takk fyrir að spila")
        on = False

    if len(spilastokkur) == 0:
        print("\nSpilastokkurinn kláraðist")
        for a in kastbunki:
            spilastokkur.append(a)
        print("Bunkinn hefur verið snúinn við og er nú stokkurinn")
    if len(spilNotandi) > 2:
        olsen = False
        olsenolsen = False
