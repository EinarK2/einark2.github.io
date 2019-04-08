# Einar Karl Pétursson
# 2/4/2019
import math


# Klasar:
# Klasinn Hringur hefur eiginleikann radíus
class Hringur:
    def __init__(self, r):  # Smiður
        self.radius = r  # Skilgreini Radiusinn

    def ummal(self):  # Skilar ummál
        return 2*self.radius*math.pi

    def flatarmal(self):  # Skilar Flatarmál
        return 2*pow(self.radius, 2)*math.pi

    def rummal(self):  # Skilar Flatarmál
        return 3*(pow(self.radius, 3)*math.pi)/4


# Klasinn Jöfnur hefur eiginleikana x og z
class Jofnur:
    def __init__(self, x, z):  # Skilgreini x og z með smiði
        self.x = x
        self.z = z

    def gildiy(self):  # Skilar eftirfarandi
        return 3*self.x+4+pow(self.x*2, 3)

    def gildiy2(self):  # Skilar eftirfarandi
        return (pow(self.z, 2) + pow(self.x, 2))*4


# Klasinn Hnit hefur eiginleikana x og y
class Hnit:
    def __init__(self, x, y):  # Skilgreini x og y með smiði
        self.x = x
        self.y = y

    def __str__(self):  # Skilar eftirfarandi sem default fyrir klasann (print)
        return "X gildi er: "+str(self.x)+" og Y gildi er: "+str(self.y)

    def stystaleid(self, t2):  # Finnur stystu leið á milli tveggja hnita
        return math.sqrt(abs(pow(self.x-t2.x, 2)) + abs(pow(self.y-t2.y, 2)))

    def hvadahluti(self):  # Segir til um hvar hnit eru
        if self.x > 0 and self.y > 0:   # Miðað við:
            print("Hnitin eru í hluta 2")  # 1|2
        elif self.x > 0 and self.y < 0:    # 3|4
            print("Hnitin eru í hluta 4")
        elif self.x < 0 and self.y < 0:
            print("Hnitin eru í hluta 3")
        elif self.x < 0 and self.y > 0:
            print("Hnitin eru í hluta 1")
        else:
            print("Óskilgreind villa")


# Valmynd:
val = ""  # Skilgreini val
while val != "0":  # Keyrir á meðan val er ekki 0
    print("1. \n2. ")
    val = input("Veldu 1 2 eða 0 til að hætta ")
    if val == "1":
        h1 = Hringur(int(input("Sláðu inn radíus hrings ")))
        print("Ummál hrings er:", round(h1.ummal(), 4))  # Prentir tölu með 4 aukastöfum
        print("Flatamál hrings er:", round(h1.flatarmal(), 4))
        print("Rúmmál hrings er:", round(h1.rummal(), 4))

        x, z = map(int, input("Sláðu inn x og z: ").split(" "))  # Bið um x og z í einu inputi
        xz = Jofnur(x, z)  # Skilgreini x og z sem eitt gildi
        print("Fyrra y er:", xz.gildiy())
        print("Seinna y er:", xz.gildiy2())

    elif val == "2":
        x, y = map(int, input("Sláðu inn hnit: ").split(" "))  # Bið um x og y í einu inputi
        xy = Hnit(x, y)  # Skilgreini x og y sem eitt gildi
        print(xy)
        xy.hvadahluti()
        x2, y2 = map(int, input("Sláðu inn önnur hnit: ").split(" "))
        xy2 = Hnit(x2, y2)
        print(xy2)
        xy2.hvadahluti()
        print("Stysta leiðin milli þeirra er:", round(xy.stystaleid(xy2), 2))

    elif val == "0":
        print("Ókei bæ")
    else:
        print("Rangur Innsláttur")