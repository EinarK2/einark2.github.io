#Höfundur Einar Karl

val=" "
while val !="6":
    print("1. N í orði")
    print("2. Nöfn")
    print("3. Samhverfu nafn")
    print("4. Texti")
    print("5. Random")
    print("6. Hætta")
    val=input("Veldu 1-5 eða 6 til að hætta ")
    if val=="1":
        texti=input("Sláðu inn texta ")
        n=texti.count('n')
        print("Það eru",n,"í textanum")
    elif val=="2":
        nafn1=input("Nafn 1: ")
        nafn2=input("Nafn 2: ")
        if len(nafn1) == len(nafn2):
            print("Nöfnin eru jafn löng")
            for x in range(len(nafn1)):
                if(nafn1[x] == nafn2[x]):
                    print("Bókstafur númer",x+1,nafn1[x],"er eins í báðum nöfnum")
        if len(nafn1) < len(nafn2):
            for x in range(len(nafn1)):
                if(nafn1[x] == nafn2[x]):
                    print("Bókstafur númer",x+1,nafn1[x],"er eins í báðum nöfnum")
        if len(nafn2) < len(nafn1):
            for x in range(len(nafn2)):
                if(nafn2[x] == nafn1[x]):
                    print("Bókstafur númer",x+1,nafn1[x],"er eins í báðum nöfnum")
    elif val=="3":
        nafn=input("Nafn: ")
        nfan=nafn[::-1]
        if nafn == nfan:
            print("Þetta nafn er samhverfu nafn")
        else:
            print("Þetta nafn er ekki samhverfu nafn")
    elif val=="4":
        texti=input("Sláðu inn texta ")
        val2=" "
        while val2 !="0":
            print("1.	Finnur og skrifar út hversu mörg orð eru í textanum.")
            print("2.	Athugaðu hvort ákveðið orð eða orðhluti er í strengnum og skrifaðu út svarið.")
            print("3.	Segir hvað strengurinn er langur sem notandinn sló inn")
            print("4.	Snýr strengnum sem sleginn var inn við og prentar hann út.")
            print("5.	Setur allan strenginn sem notandinn sló inn í stóra stafi og prentar út.")
            print("6.	Biður um staf og athugar hvort hann komi fyrir í strengnum.")
            print("7.	Setur stórt A í staðinn fyrir öll lítil a sem koma fyrir í strengnum. Hér er gott að nota replace()")
            print("0. Hættir í forritinu")
            val2=input("Veldu 1-7 eða 0 til að hætta ")
            if val2=="1":
                print("Það eru",len(texti.split()),"orð í textanum")
            elif val2=="2":
                athuga=input("Sláðu inn orð: ")
                if athuga in texti:
                    print("Orðið",athuga,"er í strengum þínum")
                else:
                    print("Orðið",athuga,"er ekki í strengum þínum")
            elif val2=="3":
                print("Strengurinn er svona langur: ",len(texti))
            elif val2=="4":
                itxet=texti[::-1]
                print("Strengurinn öfugur:",itxet)
            elif val2=="5":
                TEXTI=texti.upper()
                print("Strengurinn í hástöfum er:",TEXTI)
            elif val2=="6":
                stafur=input("Sláðu inn einn staf: ")
                if stafur in texti:
                    print("Stafurinn kemst fyrr í strenginn")
                else:
                    print("Stafurinn kemst ekki fyrir í strenginn")
            elif val2=="7":
                nyr=texti.replace('A','a')
                print("Hér er nýji strengurinn:",nyr)
            elif val2=="0":
                print("Bæjó")
            else:
                print("Rangur Innsláttur")
    elif val=="5":
        import random
        randomlisti = []
        for x in range(100):
            tala = random.randint(250, 400)
            randomlisti.append(tala)
        minnsta=min(randomlisti)
        lenminnsta=len(randomlisti)
        medaltal = sum(randomlisti) / len(randomlisti)
        print("Meðaltal talna", round(medaltal, 2))
        undir267=0
        for tala in randomlisti:
            if tala < 267:
                undir267=undir267+1
        print("Fjöldi talna undir 267:",undir267)
        print("Minnsta talan er =", minnsta,"og hún kom",lenminnsta,"sinnum")
        milli=0
        for tala in randomlisti:
            if tala > 300 and tala < 350:
                milli=milli+1
        print("Fjöldi talna milli 300 og 350 er:",milli)
        for tala in randomlisti:
            print(tala,end=" ")
        #randomlisti.sort()
        #print(randomlisti)
    elif val=="6":
        print("Ókei bæ")
    else:
        print("Rangur Innsláttur")
        
    
