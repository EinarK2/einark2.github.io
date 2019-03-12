#Einar Karl P
#29.01.2019
import math
def reiknaRummalKulu(radius):
    utk=(4.0*math.pi*(math.pow(radius,3)))/3.0
    return utk
def reiknaRummalKassa(lengd,breidd,haed):
    utk=lengd*breidd*haed
    return utk
def reiknaFlatarmalTrihyrnings(breidd,haed):
    utk=(breidd*haed)/2.0
    return utk
#Valmynd
val=" "
while val!="4":
    print("1. Reikna rúmmál kúlu")
    print("2. Reikna rúmmál kassa")
    print("3. Reikna flatarmál þríhyrnings")
    print("4. Hætta")
    val=input("Veldu ")
    if val=="1":
        rad=float(input("Sláðu inn radíus kúlu "))
        print(reiknaRummalKulu(rad))
    elif val=="2":
        lengd=float(input("Sláðu inn lengd kassa "))
        breidd=float(input("Sláðu inn breidd kassa "))
        haed=float(input("Sláðu inn hæð kassa "))
        print(reiknaRummalKassa(lengd,breidd,haed))
    elif val=="3":
        breidd = float(input("Sláðu inn breidd þríhyrnings "))
        haed = float(input("Sláðu inn hæð þríhyrnings "))
        print(reiknaFlatarmalTrihyrnings(breidd,haed))
    elif val=="4":
        print("Ókei bæ")
    else:
        print("Rangur innsláttur")
