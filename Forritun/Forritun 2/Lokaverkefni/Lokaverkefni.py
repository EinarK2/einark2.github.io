# Einar Karl Pétursson
# 30/4/2019 - 13/5/2019
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
    print(l[0])


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
                x.nr = 8  # Breytir í 8 til öryggis
                sett = spil.pop(spil.index(x))  # tekur spil úr hendi
                bunki.insert(0, sett)  # setur spil í bunka
                gert = True  # Staðfestir að það var gert
                break
            elif randtegund == 2:
                print("Tölva setti út", x, "og breytti í Spaða")
                x.tegund = 2
                x.nr = 8
                sett = spil.pop(spil.index(x))  # sama
                bunki.insert(0, sett)
                gert = True
                break
            elif randtegund == 3:
                print("Tölva setti út", x, "og breytti í Tígul")
                x.tegund = 3
                x.nr = 8
                sett = spil.pop(spil.index(x))  # sama
                bunki.insert(0, sett)
                gert = True
                break
            elif randtegund == 4:
                print("Tölva setti út", x, "og breytti í Lauf")
                x.tegund = 4
                x.nr = 8
                sett = spil.pop(spil.index(x))  # sama
                bunki.insert(0, sett)
                gert = True
                break
        elif x.tegund == bunki[0].tegund or x.nr == bunki[0].nr:  # Annars er gáð hvort spil er svipað og spil á borði
            sett = spil.pop(spil.index(x))  # Tekur spil úr hendi
            bunki.insert(0, sett)  # Setur spil í bunka
            gert = True  # Staðfestir að það var geret
            print("Tölva setti út", sett)  # Skrifað hvað gert var
            break
    if gert == False:  # Ef ekki var gert
        spil.append(stokkur.pop(0))  # Dregur spil
        if spil[-1].nr == 8:  # Gáir hvort eih spil er 8
            randtegund = random.randint(1, 4)  # Tekur random tölu fyrir tegund
            if randtegund == 1:
                print("Tölva dróg einu sinni")
                print("Tölva setti út", spil[-1], "og breytti í Hjarta")
                spil[-1].tegund = 1  # Breytir tegund í 1 (Hjarta)
                spil[-1].nr = 8  # Breytir í 8 til öryggis
                sett = spil.pop(-1)  # tekur spil úr hendi
                bunki.insert(0, sett)  # setur spil í bunka
            elif randtegund == 2:
                print("Tölva dróg einu sinni")
                print("Tölva setti út", spil[-1], "og breytti í Spaða")
                spil[-1].tegund = 2
                spil[-1].nr = 8
                sett = spil.pop(-1)  # sama
                bunki.insert(0, sett)
            elif randtegund == 3:
                print("Tölva dróg einu sinni")
                print("Tölva setti út", spil[-1], "og breytti í Tígul")
                spil[-1].tegund = 3
                spil[-1].nr = 8
                sett = spil.pop(-1)  # sama
                bunki.insert(0, sett)
            elif randtegund == 4:
                print("Tölva dróg einu sinni")
                print("Tölva setti út", spil[-1], "og breytti í Lauf")
                spil[-1].tegund = 4
                spil[-1].nr = 8
                sett = spil.pop(-1)  # sama
                bunki.insert(0, sett)
        elif spil[-1].nr == bunki[0].tegund or spil[-1].tegund == bunki[0].tegund:  # Gáir hvort það spil kemst á borð
            sett = spil.pop(-1)  # Tekur það
            bunki.insert(0, sett)  # Setur í bunka
            print("Tölva dróg einu sinni")
            print("Tölva setti út", sett)
        else:  # Gerir sama aftur ef spilið kemst ekki
            spil.append(stokkur.pop(0))
            if spil[-1].nr == 8:  # Gáir hvort eih spil er 8
                randtegund = random.randint(1, 4)  # Tekur random tölu fyrir tegund
                if randtegund == 1:
                    print("Tölva dróg tvisvar")
                    print("Tölva setti út", spil[-1], "og breytti í Hjarta")
                    spil[-1].tegund = 1  # Breytir tegund í 1 (Hjarta)
                    spil[-1].nr = 8  # Breytir í 8 til öryggis
                    sett = spil.pop(-1)  # tekur spil úr hendi
                    bunki.insert(0, sett)  # setur spil í bunka
                elif randtegund == 2:
                    print("Tölva dróg tvisvar")
                    print("Tölva setti út", spil[-1], "og breytti í Spaða")
                    spil[-1].tegund = 2
                    spil[-1].nr = 8
                    sett = spil.pop(-1)  # sama
                    bunki.insert(0, sett)
                elif randtegund == 3:
                    print("Tölva dróg tvisvar")
                    print("Tölva setti út", spil[-1], "og breytti í Tígul")
                    spil[-1].tegund = 3
                    spil[-1].nr = 8
                    sett = spil.pop(-1)  # sama
                    bunki.insert(0, sett)
                elif randtegund == 4:
                    print("Tölva dróg tvisvar")
                    print("Tölva setti út", spil[-1], "og breytti í Lauf")
                    spil[-1].tegund = 4
                    spil[-1].nr = 8
                    sett = spil.pop(-1)  # sama
                    bunki.insert(0, sett)
            elif spil[-1].nr == bunki[0].tegund or spil[-1].tegund == bunki[0].tegund:
                sett = spil.pop(-1)
                bunki.insert(0, sett)
                print("Tölva dróg tvisvar")
                print("Tölva setti út", sett)
            else:  # Gerir sama aftur
                spil.append(stokkur.pop(0))
                if spil[-1].nr == 8:  # Gáir hvort eih spil er 8
                    randtegund = random.randint(1, 4)  # Tekur random tölu fyrir tegund
                    if randtegund == 1:
                        print("Tölva dróg þrisvar")
                        print("Tölva setti út", spil[-1], "og breytti í Hjarta")
                        spil[-1].tegund = 1  # Breytir tegund í 1 (Hjarta)
                        spil[-1].nr = 8  # Breytir í 8 til öryggis
                        sett = spil.pop(-1)  # tekur spil úr hendi
                        bunki.insert(0, sett)  # setur spil í bunka
                    elif randtegund == 2:
                        print("Tölva dróg þrisvar")
                        print("Tölva setti út", spil[-1], "og breytti í Spaða")
                        spil[-1].tegund = 2
                        spil[-1].nr = 8
                        sett = spil.pop(-1)  # sama
                        bunki.insert(0, sett)
                    elif randtegund == 3:
                        print("Tölva dróg þrisvar")
                        print("Tölva setti út", spil[-1], "og breytti í Tígul")
                        spil[-1].tegund = 3
                        spil[-1].nr = 8
                        sett = spil.pop(-1)  # sama
                        bunki.insert(0, sett)
                    elif randtegund == 4:
                        print("Tölva dróg þrisvar")
                        print("Tölva setti út", spil[-1], "og breytti í Lauf")
                        spil[-1].tegund = 4
                        spil[-1].nr = 8
                        sett = spil.pop(-1)  # sama
                        bunki.insert(0, sett)
                elif spil[-1].nr == bunki[0].tegund or spil[-1].tegund == bunki[0].tegund:
                    sett = spil.pop(-1)
                    bunki.insert(0, sett)
                    print("Tölva dróg þrisvar")
                    print("Tölva setti út", sett)
                else:  # Ef dregið er þrisvar og ekki hægt að gera
                    print("Tölva dróg þrisvar og sagði pass")


tilvik = Spil(0, 0)
spilastokkur = tilvik.geraSpilaStokk()  # Gerir spilastokk
# synaspil(spilastokkur)  # ef þú vilt sýna spil

spilNotandi = []  # skilgreinir notanda, tölvu og bunka
spilTolva = []
kastbunki = []

for x in range(5):  # Tekur úr stokk (keyrir 5 sinnum)
    spilNotandi.append(spilastokkur.pop(0))  # Gefur Notanda spil
    spilTolva.append(spilastokkur.pop(0))  # Gefur tölvu spil

kastbunki.append(spilastokkur.pop(0))  # Tekur úr stokk og setur á borð

# spilbord(kastbunki)  # Sýnir borð

print("\nLeiðbeiningar:\n\nSkrifaðu 'draga' til að draga og 'pass' ef þú getur ekki dregið meir")
print("\nSkrifaðu 'olsen' þegar þú ert með 2 spil eftir og getur sett eitt")
print("og 'olsen olsen' þegar þú ert með 1 spil eftir og getur sett það")
print("\nEf þú færð 8 geturu alltaf sett hana og þá geturu breytt um tegund spils")
print("\nTil að velja spil þarf að slá inn tölu eftir röð spilanna (1,2,3,4...)")
dragatel = 0  # skilgreini teljara og annað
on = True
draga = True
olsen = False
olsenolsen = False
while on:  # Keyrir á meðan on = True
    print()
    spiltolvu(spilTolva)  # Sýnir spil tölvu
    spilhendi(spilNotandi)  # Sýnir spil notanda
    spilbord(kastbunki)  # Sýnir borð
    print()
    ut = input("Hvaða spil viltu setja? Þú getur líka gert draga/pass/olsen/olsen olsen : ")
    if ut == "draga":  # Ef skrifað er draga
        for x in spilNotandi:  # Fer í gegnum spil í notanda
            if x.nr == 8:  # Ef spilið er 8
                print("\nÞú mátt ekki draga (Þú getur sett 8)")
                draga = False  # Má ekki draga
                break
            elif kastbunki[0].tegund == x.tegund or kastbunki[0].nr == x.nr:  # Ef spilið er svipað og spil á borði
                print("\nÞú mátt ekki draga")
                draga = False  # Má ekki draga
                break
            else:  # Annars
                draga = True  # Má draga
        if draga == True:  # Ef notandi má draga
            dragatel += 1  # Bætt við á Teljari fyrir hversu oft er dregið
            if dragatel == 4:  # Ef teljarinn er kominn í 4 má ekki draga
                print("\nÞú mátt ekki draga meir gerðu pass")
            else:  # Annars
                spilNotandi.append(spilastokkur.pop(0))  # Tekur spil úr stokk og setur á hendi
                print("\nÞú drógst", spilNotandi[-1])  # Segir hvað dregið var

    elif ut == "pass":  # Ef skrifað var pass
        for x in spilNotandi:  # Fer í gegnum spil notanda
            if x.nr == 8:  # Ef spil er 8
                print("\nÞú mátt ekki gera pass (Þú getur sett 8)")
                break
        if dragatel < 3:  # Ef teljari fyrir að draga er minna en 3 má ekki gera pass
            print("\nÞú getur ekki gert pass")
        if dragatel == 4 or dragatel == 3:  # Ef það er 3 eða 4 má gera pass
            print("\nÞú gerðir pass")
            dragatel = 0  # Endurstillir teljara
            tolvagerir(spilTolva, kastbunki, spilastokkur)  # Tölva gerir

    elif ut == "olsen":  # Ef skrifað er olsen
        if len(spilNotandi) == 2:  # Ef það eru 2 spil eftir á hendi
            print("\nVel gert, settu nú spilið")
            olsen = True  # Olsen er núna True
        else:  # Annars
            print("\nÞú mátt ekki segja olsen")
    elif ut == "olsen olsen":  # Ef skrifað er olsen olsen
        if len(spilNotandi) == 1:  # Ef eitt spil er eftir
            print("\nVel gert, settu nú spilið")
            olsenolsen = True  # olsenolsen er True
        else:  # Annars
            print("\nÞú mátt ekki segja olsen olsen")

    else:  # Allt annað, semsagt tölur
        try:  # Reynir að gera eftirfarandi
            ut = int(ut)  # Breytir input í tölu
            if spilNotandi[ut-1].nr == 8:  # Ef talan sem var valin er 8
                print("\nÞú settir út", spilNotandi[ut - 1])
                flag = True
                while flag:  # Keyrir í gegnum þetta þangað til rétt input er skrifað
                    breyta = input("Fyrst spilið er 8 hvað viltu breyta spilinu í? (hjarta/spaði/tígull/lauf): ")
                    if breyta == "hjarta":  # Ef skrifað er hjarta
                        spilNotandi[ut-1].tegund = 1  # Breytir tegund í hjarta til að vera viss
                        spilNotandi[ut - 1].nr = 8  # Breytir númeri líka í 8 til að vera viss
                        settUt = spilNotandi.pop(ut - 1)  # Tekur spilið
                        kastbunki.insert(0, settUt)  # Setur það í bunka
                        flag = False  # Lokar lúppunni
                    elif breyta == "spaði":  # SAMA
                        spilNotandi[ut - 1].tegund = 2
                        spilNotandi[ut - 1].nr = 8
                        settUt = spilNotandi.pop(ut - 1)
                        kastbunki.insert(0, settUt)
                        flag = False
                    elif breyta == "tígull":  # SAMA
                        spilNotandi[ut - 1].tegund = 3
                        spilNotandi[ut - 1].nr = 8
                        settUt = spilNotandi.pop(ut - 1)
                        kastbunki.insert(0, settUt)
                        flag = False
                    elif breyta == "lauf":  # SAMA
                        spilNotandi[ut - 1].tegund = 4
                        spilNotandi[ut - 1].nr = 8
                        settUt = spilNotandi.pop(ut - 1)
                        kastbunki.insert(0, settUt)
                        flag = False
                    else:  # Annars
                        print("Rangur Innsláttur")
                        flag = True  # Keyrir enn
                if len(spilNotandi) == 0:  # Ef ekkert spil er á hendi
                    print("Til hamingju þú vannst, takk fyrir að spila")  # Vinnur
                    on = False  # Lokar on lúppu
                else:  # Annars gerir tölva
                    dragatel = 0  # Endurstillir líka draga teljara alltaf þegar tölva gerir
                    tolvagerir(spilTolva, kastbunki, spilastokkur)
            elif kastbunki[0].tegund == spilNotandi[ut-1].tegund or kastbunki[0].nr == spilNotandi[ut-1].nr:
                print("\nÞú settir út", spilNotandi[ut - 1])  # Ef spil er svipað og á borði
                settUt = spilNotandi.pop(ut-1)  # Tekur spil
                kastbunki.insert(0, settUt)  # Setur í bunka
                if len(spilNotandi) == 0:  # Ef ekkert er á hendi
                    print("Til hamingju þú vannst, takk fyrir að spila")  # Vinnur
                    on = False  # Lokar on lúppu
                else:
                    # Tölva gerir
                    dragatel = 0
                    tolvagerir(spilTolva, kastbunki, spilastokkur)
            else:  # Annars
                print("Þú getur ekki sett út þetta spil")
        except:  # Ef ekkert af ofan virkaði (eih rugl skrifað)
            print("Þetta er ekki þekkt skipun")

    if olsen == False and len(spilNotandi) == 1:  # Ef olsen er False og eitt spil er á hendi
        print("\nÞú gleymdir að segja olsen svo þú færð 3 spil")
        spilNotandi.append(spilastokkur.pop(0))  # Dregur spil 3 sinnum:
        print("Þú drógst", spilNotandi[-1])
        spilNotandi.append(spilastokkur.pop(0))
        print("Þú drógst", spilNotandi[-1])
        spilNotandi.append(spilastokkur.pop(0))
        print("Þú drógst", spilNotandi[-1])

    if olsenolsen == False and len(spilNotandi) == 0:  # Ef olsenolsen er False og ekkert spil er á hendi
        print("\nÞú gleymdir að segja olsen olsen svo þú færð 3 spil")
        spilNotandi.append(spilastokkur.pop(0))  # Dregur spil 3 sinnum:
        print("Þú drógst", spilNotandi[-1])
        spilNotandi.append(spilastokkur.pop(0))
        print("Þú drógst", spilNotandi[-1])
        spilNotandi.append(spilastokkur.pop(0))
        print("Þú drógst", spilNotandi[-1])

    if len(spilTolva) == 0:  # ef engin spil eru á hendi tölvu
        print("Tölva vann, takk fyrir að spila")
        on = False  # lokar lúppu

    if len(spilastokkur) == 0:  # Ef ekkert er eftir í stokknum
        print("\nSpilastokkurinn kláraðist")
        for a in kastbunki:  # Fer í gegnum bunka
            spilastokkur.append(a)  # Setur spil úr bunka í stokk
        print("Bunkinn hefur verið snúinn við og er nú stokkurinn")
    if len(spilNotandi) > 2:  # Ef spil á hendi eru meiri en 2
        olsen = False  # Gerir olsen og olsenolsen sem false
        olsenolsen = False
