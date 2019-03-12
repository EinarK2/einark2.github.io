#Höfundur Einar Karl Pétursson
#5/2/2019
import math
import random
#Def:
#1
def farenheit(cel):
    utkoma = cel*1.8+32 #Reiknar hvað celsíus er í fahrenheit með formúlu
    return utkoma #Skilar útreikninginn
def celsius(faren):
    utkoma = (faren-32)/1.8 #Reiknar hvað fahrenheit er í celsíus með formúlu
    return utkoma #Skilar útreikninginn
#2
def kelvin(cel):
    utkoma = cel+273.15 #Finnur hvað celsíus er í kelvin með formúlu
    return utkoma #Skilar útreikninginn
def celsiusKelvin(kel):
    utkoma = kel-273.15 #finnur hvað kelvin er í celsíus með formúlu
    return utkoma #Skilar útreikninginn
#3
def reiknaVeldi(tala, veldi):
    utkoma=math.pow(tala,veldi) #Tekur tvær tölur og notar math til að finna veldi fyrri tölunnar
    return utkoma #Skilar útreikninginn
#4
def sentimetrar(tomm):
    utkoma=tomm*2.54 #Finnur hvað tommur eru í sentimetrum með formúlu
    return utkoma #Skilar útreikninginn
def tommur(cm):
    utkoma=cm/2.54 #finnur hvað sentimetrar eru í tommum með formúlu
    return utkoma #Skilar útreikninginn
#5
def liter(gall):
    utkoma=gall*3.785 #Finnur hvað gallon eru í lítrum með formúlu
    return utkoma #Skilar útreikninginn
def gallon(litrar):
    utkoma=litrar/3.785 #Finnur hvað lítrar eru í gallonum með formúlu
    return utkoma #Skilar útreikninginn
#6
def nafnogkyn(nafn, kyn):#Tekur nafn og kyn
    if kyn=="kk": #Ef kyn er karlkyn prentar það eftirfarandi (með nafni)
        print("Sæll og blessaður",nafn)
    elif kyn=="kvk": #Sama nema með kvenkyni
        print("Sæl og blessuð",nafn)
    else: #Prentar eftirfarandi ef kk eða kvk er ekki skrifað
        print("Þetta kyn þekki ég ekki")
#7
def kasta():
    slembitala = random.randint(1, 6) #Finnur einhverja tölu á skalanum 1 til 6
    return slembitala #Skilar útreikninginn
#8
def listar():
    listi1=[] #Skilgreinir lista 1
    for x in range(10): #Þessi forlúppa finnur 10 handahófskenndar tölur og setur þær í lista 1
        tala = random.randint(1, 25)
        listi1.append(tala)
    listi2 = [] #Skilgreinir lista 2
    for y in range(10): #Þessi forlúppa gerir sama og hin en setur í lista 2
        tala = random.randint(1, 25)
        listi2.append(tala)
    listi3=[] #Skilgreinir lista 3
    for i in listi1: #Þessi forlúppa finnur tölur sem eru eins í lista 1 og 2 og setur þær í lista 3
        for a in listi2:
            if i==a:
                listi3.append(i)
    return listi3 #Skilar lista 3
#Valmynd
val=""
while val !="9":
    print("1. Celsíus og Fahrenheit")
    print("2. Celsíus og Kelvin")
    print("3. Veldareikningur")
    print("4. Tommur og Sentimetrar")
    print("5. Gallon og lítrar")
    print("6. Kveðja")
    print("7. Teningakast")
    print("8. Listar")
    print("9. Hætta")
    val=input("Veldu 1-8 eða 9 til að hætta ")
    if val=="1":
        cf=input("Hvort viltu breyta Celsíus í Fahrenheit eða Fahrenheit í Celsíus? (c/f) ") #cf er celsíus fahrenheit
        if cf=="c": #Ef Valið var Celsíus
            cel=float(input("Sláðu inn celsíus: "))
            print(farenheit(cel))
        elif cf=="f": #Ef valið var Fahrenheit
            faren=float(input("Sláðu inn fahrenheit: "))
            print(celsius(faren))
    elif val=="2":
        ck = input("Hvort viltu breyta Celsíus í Kelvin eða Kelvin í Celsíus? (c/k) ") #ck er celsíus kelvin
        if ck == "c": #Ef valið var celsíus
            cel = float(input("Sláðu inn celsíus: "))
            print(kelvin(cel))
        elif ck == "k": #ef valið var kelvin
            kel = float(input("Sláðu inn kelvin: "))
            print(celsiusKelvin(kel))
    elif val=="3":
        tala=float(input("Sláðu inn grunntölu "))
        veldi=float(input(("Sláðu inn veldistölu ")))
        print(reiknaVeldi(tala, veldi))
    elif val=="4":
        ts=input("Hvort viltu breyta Tommur í sentimetra eða sentimetra í tommur? (t/s) ") #ts merkir tommur og sentimetrar
        if ts=="t": #ef valið var tommur
            tomm=float(input("Sláðu inn tommur: "))
            print(sentimetrar(tomm))
        elif ts=="s":#ef valið var sentimetrar
            cm=float(input("Sláðu inn sentimetra: "))
            print(tommur(cm))
    elif val=="5":
        gl=input("Hvort viltu breyta gallon í lítra eða lítra í gallon? (g/l)") #gl merkir gallon og sentimetrar
        if gl=="g": #ef valið var gallon
            gall=float(input("Sláðu inn gallon: "))
            print(liter(gall))
        elif gl=="l":#ef valið var lítrar
            litrar=float(input("Sláðu inn lítra: "))
            print(gallon(litrar))
    elif val=="6":
        nafn=input("Hvert er nafn þitt? ")
        kyn=input("Hvert er þitt kyn? (kk/kvk) ")
        nafnogkyn(nafn, kyn)
    elif val=="7":
        print(kasta())
    elif val=="8":
        print(listar())
    elif val=="9":
        print("Ókei bæ")
    else:
        print("Rangur Innsláttur") #Bara ef skrifað er annað en það sem beðið var um