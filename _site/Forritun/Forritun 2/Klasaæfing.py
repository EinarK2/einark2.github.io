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

    def elsti(self, listinem):
        pass

    def rada(self, listinem):
        pass

    def fjoldiBraut(self, listinem):
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
        for x in range(2):
            nafn = input("Sláðu inn Nafn í símaskrá ")
            gsm = int(input("Sláðu inn GSM "))
            simi = int(input("Sláðu inn heimasíma "))
            email = input("Sláðu inn Email ")
            t = Medlimir(nafn, gsm, simi, email)
            medlimaListi.append(t)
        for x in medlimaListi:
            print(x)
        medlimaListi[0].setNafn("Einar Karl")
        medlimaListi[0].setGsm(6948820)
        medlimaListi[0].setHeimasimi(5643103)
        medlimaListi[0].setEmail("einarkarlp@gmail.com")
        print("breytt:\n", medlimaListi[0])

    elif val == "3":
        listinem = []
        for x in range(2):
            nafn = input("Sláðu inn nafn Nemanda: ")
            aldur = int(input("Sláðu inn Aldur: "))
            braut = input("Sláðu inn braut: ")
            t = Nemandi(nafn, aldur, braut)
            listinem.append(t)
        tel = 1
        for x in listinem:
            print("Nemandi", tel, ":")
            print(x)
            tel += 1
    elif val == "4":
        pass
    elif val == "5":
        print("Ókei Bæ")
    else:
        print("Rangur Innsláttur")
