# Höfundur Einar Karl

val = " "
while val != "8":
    print("1. Tölur")
    print("2. Nafn og Aldur")
    print("3. ")
    print("4. ")
    print("5. ")
    print("6. ")
    print("7. ")
    print("8. Hætta")
    val = input("Veldu 1-7 eða 8 til að hætta ")
    if val == "1":
        tala1 = int(input("Sláðu inn tölu 1"))
        tala2 = int(input("Sláðu inn tölu 2"))
        tala3 = int(input("Sláðu inn tölu 3"))
        if tala1 > tala2 and tala1 > tala3:
            pass

    elif val == "2":
        import datetime
        nuna=datetime.datetime.now()
        arNuna=nuna.year
        fjAraAldamot=2100-arNuna
        nafn=input("Hvað heitir þú? ")
        aldur=int(input("Hversu gamall ert þú? "))
        print(nafn+", um næstu aldamót verður þú:",aldur+fjAraAldamot,"ára")
    elif val == "3":
        print("Slegið er inn tölur þangað til slegið er inn 0. Þá færðu niðurstöður")
        tala=()
        listi=[]
        while tala!=int(0):
            tala=int(input(": "))
            listi.append(tala)
        print("Summa talnanna er:",sum(listi))
        print("Fjöldi talna sem slegin var inn:",len(listi))
        medaltal = sum(listi) / len(listi)
        print("Meðaltal talnanna:",round(medaltal,2))

    elif val == "4":
        import math #math.pi
        kula=int(float(input("Radíus kúlunnar? ")))
        surface=4*math.pi*(math.pow(kula,2))
        rummal=(4*(math.pow(kula,3))*math.pi)/3
        print("Yfirborðsflatarmál kúlunnar er:",round(surface,5))
        print("Rúmmál kúlunnar er:",round(rummal,5))
    elif val == "5":
        lykilord=input("Sláðu inn lykilorð og forritið mun athuga hvort það er löglegt eða ekki ")
        if len(lykilord) < 6:
            print("Þetta lykilorð er of stutt")
        else:
            tolustafur=False
            bokstafur=False
            for x in lykilord:
                if x.isdigit()==True:
                    tolustafur=True
                if x.isalpha()==True:
                    bokstafur=True
            if tolustafur==True and bokstafur==True:
                print("Lykilorðið okkar er í lagi")
            else:
                print("Þú þarft bæði bókstafi og tölustafi í lykilorðið")
    elif val == "6":
        texti=input("Sláðu inn texta ")
        hastafir=0
        lagstafir=0
        for x in texti:
            if x.islower()==True:
                lagstafir=lagstafir+1
            if x.isupper()==True:
                hastafir=hastafir+1
        print("Í þessum texta eru",hastafir,"hástafir",lagstafir,"lágstafir")
    elif val == "7":
        tala1=int(input("Sláðu inn tölu 1 "))
        tala2=int(input("Sláðu inn tölu 2 "))
        samnefnari = 0
        if tala1 >0 and tala2 >0:
            for x in range(1,100):
                if tala1 %x ==0 and tala2 %x ==0:
                    samnefnari=x
        else:
            print("Það má ekki nota núll í þessum lið")
        print("Stærsti samnefnarinn",samnefnari)
    elif val == "8":
        print("Ókei bæ")
    else:
        print("Rangur Innsláttur")
