# Einar Karl Pétursson
# 2/4/2019
import math


# Klasar:
# Klasinn Hringur hefur eiginleikann radíus
class Hringur:
    def __init__(self, r): # Smiður
        self.radius = r

    def ummal(self):
        return 2*self.radius*math.pi

    def flatarmal(self):
        return 2*pow(self.radius, 2)*math.pi

    def rummal(self):
        return 3*(pow(self.radius, 3)*math.pi)/4


# Klasinn Jöfnur hefur eiginleikana x og z
class Jofnur:
    def __init__(self, x, z):
        self.x = x
        self.z = z

    def gildiy(self):
        return 3*self.x+4+pow(self.x*2, 3)

    def gildiy2(self):
        return (pow(self.z, 2) + pow(self.x, 2))*4


# Klasinn Hnit hefur eiginleikana x og y
class Hnit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "X gildi er: "+str(self.x)+" og Y gildi er: "+str(self.y)

    def stystaleid(self, t2):
        return math.sqrt(abs(pow(self.x-t2.x, 2)) + abs(pow(self.y-t2.y, 2)))

    def hvadahluti(self):
        if self.x > 0 and self.y > 0:
            print("Hnitin eru í hluta 2")
        elif self.x > 0 and self.y < 0:
            print("Hnitin eru í hluta 4")
        elif self.x < 0 and self.y < 0:
            print("Hnitin eru í hluta 3")
        elif self.x < 0 and self.y > 0:
            print("Hnitin eru í hluta 1")
        else:
            print("what")

val = ""
while val != "0":
    print("1. \n2. ")
    val = input("Veldu 1 2 eða 0 til að hætta ")
    if val == "1":
        h1 = Hringur(int(input("Sláðu inn radíus hrings ")))
        print("Ummál hrings 1 er:", round(h1.ummal(), 4))
        print("Flatamál hrings 1 er:", round(h1.flatarmal(), 4))
        print("Rúmmál hrings 1 er:", round(h1.rummal(), 4))

        x, z = map(int, input("Sláðu inn x og z: ").split(" "))
        xz = Jofnur(x, z)
        print("Fyrra y er:", xz.gildiy())
        print("Seinna y er:", xz.gildiy2())

    elif val == "2":
        x, y = map(int, input("Sláðu inn hnit: ").split(" "))
        xy = Hnit(x, y)
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