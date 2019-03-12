#Höfundur Einar Karl
val=" " #Skilgreinir val
while val !="6": #þegar sláð inn er 6 hættir while lykkjan
    print("1. Listi fyrir tölur")
    print("2. Random tölur")
    print("3. Strengjalisti")
    print("4. Fjöldi teningakasta ákveðinn af notanda")
    print("5. Skráning í áfanga")
    print("6. Hætta")
    val=input("Veldu 1-5 eða 6 til að hætta ")
    if val=="1":
        talnalisti=[]
        for x in range(7):
            tala=float(input("Sláðu inn tölu númer "+str(x+1)+" ")) #Biður um 7 tölur (for lykkja)
            talnalisti.append(tala) #setur tölurnar í lista
        medaltal = sum(talnalisti) / len(talnalisti) #reiknar meðaltal
        print("Hæðsta talan er", max(talnalisti)) #Prentar hæðstu tölu með max
        print("Lægsta talan", min(talnalisti)) #Sama nema min
        print("Meðaltal er",medaltal)
        print("Summa talnanna er", sum(talnalisti)) #reiknar summu með sum
        print("Listinn Raðaður: ")
        talnalisti.sort()  # raða listanum eftir stærð minnsta talan fyrst
        print(talnalisti)
        print("Listinn sýndur með for lúppu: ")
        for tala in talnalisti:
            print(tala, end=";") #Nota ; til að hafa á milli talnanna
        print("")
        undir50 = 0
        fjoldi=[]
        for tala in talnalisti: #Finnur allar tölur undir 50.5 og setur í lista
            if tala <= 50.5:
                fjoldi.append(tala)
                undir50 = undir50 + 1
        print("Tölur undir 50,5:",fjoldi)
        print("Fjöldi talna undir 50,5:", undir50)
    elif val=="2":
        import random
        randomlisti = []
        for x in range(70): #Keyrir 70 sinnum
            tala = random.randint(1, 500)
            randomlisti.append(tala)

        for x in range(1,len(randomlisti)): #Lúppa sem aðskilur allar tölurnar (4 tölur í línu
            if x%4==0: #Prentar þangað til að fjórar tölur eru komnar
                print(randomlisti[x])
            else: #Til að skipta um línu
                print(randomlisti[x],end="\t")
        print("")
        print("Hæðsta talan er", max(randomlisti))
        print("Minnsta talan er", min(randomlisti))
        print("Hér er listinn í öfugri röð: ")
        randomlisti.sort()
        randomlisti.reverse()
        for x in range(1,len(randomlisti)): #Sama og áðan nema 6 tölur í hverri línu
            if x%6==0:
                print(randomlisti[x])
            else:
                print(randomlisti[x],end="\t")
        print("") #Til að aðskilja síðustu línu frá þeirri næstu
        fyrri = 0 #Tölurnar á milli 1 og 250
        seinni = 0 #Tölurnar á milli 251 og 500
        for tala in randomlisti: #Telur tölurnar
            if tala > 1 and tala < 250:
                fyrri = fyrri + 1
        for tala in randomlisti: #Svipað
            if tala > 251 and tala < 500:
                seinni = seinni + 1
        print("Tölur á bilinu 1-250 eru:",fyrri)
        print("Tölur á bilinu 251-500 eru:",seinni)
    elif val=="3":
        nafnalisti=[]
        for x in range(5): #Til að spurja um 5 nöfn og setja þau í lista
            nafn = input("Sláðu inn nafn númer " + str(x + 1) + " ")
            nafnalisti.append(nafn)
        original=nafnalisti.copy() #Copy-a listann til að hafa upprunalega (svo hann breytist ekki)
        val2=" "
        while val2 !="5": #Önnur valmynd sem hættir þegar sláð inn er 5
            print("1	Birta nöfnin óraðað.")
            print("2	Raða nöfnunum í stafrófsröð og birta.")
            print("3	Raða nöfnunum í öfuga stafrófsröð og birta.")
            print("4	Birta eitt nafn eftir því hvaða númer 1-5 var valið.")
            print("5	Hætta í verkefni 3.")
            val2=input("Veldu 1-4 eða 5 til að hætta ")
            if val2=="1":
                print(original)
            elif val2=="2":
                nafnalisti.sort() #Sortar listan
                print(nafnalisti)
            elif val2=="3":
                nafnalisti.sort()
                nafnalisti.reverse()#Sortar og snýr svo við
                print(nafnalisti)
            elif val2=="4":
                val3=int(input("Veldu 1-5 "))
                val3=nafnalisti[val3-1]#Tekur númer eitthvað úr listanum(-1 er svo það er rétt)
                print(val3)
            elif val2=="5":
                print("Ókei bæ")
            else:
                print("Rangur Innsláttur")

    elif val=="4":
        import random
        oft=int(input("Hve oft viltu kasta teningnum? "))
        listinn=[]
        for x in range(oft): #Kastar teningnum og setur niðurstöður í listan
            talan=random.randint(1,6)
            listinn.append(talan)
        print("Talan 1 kom",listinn.count(1),"sinnum")
        print("Talan 2 kom",listinn.count(2),"sinnum")
        print("Talan 3 kom",listinn.count(3),"sinnum") #Telur hversu oft talan kemur
        print("Talan 4 kom",listinn.count(4),"sinnum")
        print("Talan 5 kom",listinn.count(5),"sinnum")
        print("Talan 6 kom",listinn.count(6),"sinnum")
        print("Talan",max(set(listinn), key=listinn.count),"kom oftast upp")#Telur hvaða tala kom oftast
        print("Talan",min(set(listinn), key=listinn.count), "kom sjaldnast upp") #minnst
    elif val=="5":
        afangi=int(input("Hvað er margir skráðir í hópinn FOR1TÖ05BU? "))
        allir=[]
        for x in range(afangi): #Biður um x mörg nöfn og setur í lista
            nafn = input("Sláðu inn nafn númer "+str(x+1)+" ")
            allir.append(nafn)
        allir.sort()
        for nafn in allir: #Prentar listann línu eftir línu
            print(nafn)
    elif val=="6":
        print("Ókei bæ")
    else: #Ef sláð er inn annað en 1-6
        print("Rangur Innsláttur")