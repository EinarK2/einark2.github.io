# Einar Karl Pétursson
# 21/3/2019


# Klasar:
class Setning:
    def __init__(self, str):  # Smiður
        self.strengur = str

    def __str__(self):  # String Fall
        return self.strengur


class Medlimir:
    def __init__(self, n, g, h, e):
        self.nafn = n
        self.gsm = g
        self.heimasimi = h  # ÞETTA ERU EIGINLEIKAR
        self.email = e

    def __str__(self):
        return "Nafn: "+self.nafn+". GSM: "+str(self.gsm)+". Heimasími: "+str(self.heimasimi)+". Netfang: "+self.email

    def setNafn(self, n):
        self.nafn = n

    def setGsm(self, g):
        self.gsm = g

    def setHeimasimi(self, h):
        self.heimasimi = h

    def setEmail(self, e):
        self.email = e


class Nemandi:
    def __init__(self, n, a, b):
        self.nafn = n
        self.aldur = a
        self.braut = b

    def __str__(self):
        return "Nemandi: "+self.nafn+"\nAldur: "+str(self.aldur)+"\nBraut: "+self.braut

    def elsti(listi):
        aldur = 0
        nafn = ""
        for x in listi:
            if x.aldur > aldur:
                aldur = x.aldur
                nafn = x.nafn
        print("Elsti er:", nafn, "hann er", aldur, "ára")

    def rada(listi):
        nafnalisti = []
        for x in listi:
            nafnalisti.append(x.nafn)
        nafnalisti.sort()
        print("Listinn raðaður: ", nafnalisti)

    def fjoldiBraut(listi):
        fjHar = 0
        fjTolvu = 0
        for x in listi:
            if x.braut == "hb":
                fjHar = fjHar+1
            elif x.braut == "tb":
                fjTolvu += 1
            else:
                print(x.braut)
        print("Fjöldi á tölvubraut:", fjTolvu, "\nFjöldi á hársnyrtibraut:", fjHar)


class Bankareikningur:
    def __init__(self, n, i):
        self.nafn = n
        self.inneign = i

    def __str__(self):
        return "Nafn: "+self.nafn+" Inneign: "+str(self.inneign)

    vextir = 0.04

    def reiknaInneign(listi):
        #for x in listi:
        pass
            #inneign = x.inneign*x.vextir

    def breytaArsvexti(inneign):
        pass

# Valmynd:
val = ""
while val != "5":
    print("1. \n2. \n3. \n4. \n5. Hætta")
    val = input("Veldu 1-4 eða 5 til að hætta ")
    if val == "1":
        temp = input("Sláðu inn streng ")
        s1 = Setning(temp)
        print(s1)
    elif val == "2":
        medlimaListi = []
        margir = int(input("Hve marga viltu setja í símaskránna? "))
        for x in range(margir):
            nafn = input("Sláðu inn Nafn í símaskrá ")
            gsm = int(input("Sláðu inn GSM "))
            simi = int(input("Sláðu inn heimasíma "))
            email = input("Sláðu inn Email ")
            t = Medlimir(nafn, gsm, simi, email)
            medlimaListi.append(t)
        for x in medlimaListi:
            print(x)
        breyta = ""
        while breyta != "n":
            breyta = input("Viltu breyta gsm? (j/n) ")
            if breyta == "j":
                numer = int(input("Númer hvað í skránni viltu breyta? "))
                numer -= 1
                print(numer)
                breytanafn = input("Sláðu inn Nafn ")
                breytagsm = int(input("Sláðu inn GSM "))
                breytasimi = int(input("Sláðu inn heimasíma "))
                breytaemail = input("Sláðu inn Email ")
                medlimaListi[numer].setNafn(breytanafn)
                medlimaListi[numer].setGsm(breytagsm)
                medlimaListi[numer].setHeimasimi(breytasimi)
                medlimaListi[numer].setEmail(breytaemail)
                print("Breytt:\n", medlimaListi[numer])
    elif val == "3":
        listinem = []
        margir = int(input("Hve marga nemendur viltu setja inn? "))
        for x in range(margir):
            nafn = input("Sláðu inn nafn Nemanda: ")
            aldur = int(input("Sláðu inn Aldur: "))
            braut = input("Sláðu inn braut: ")
            t = Nemandi(nafn, aldur, braut)
            listinem.append(t)
        tel = 1
        for x in listinem:
            print("-- Nemandi", tel, ":")
            print(x)
            tel += 1
        Nemandi.elsti(listinem)
        Nemandi.rada(listinem)
        Nemandi.fjoldiBraut(listinem)
    elif val == "4":
        pass
    elif val == "5":
        print("Ókei Bæ")
    else:
        print("Rangur Innsláttur")
