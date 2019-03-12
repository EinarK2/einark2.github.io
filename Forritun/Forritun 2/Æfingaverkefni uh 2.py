#Höfundur Einar Karl
#Dagsetning 1/10/2019
val=" "
while val !="7":
    print("1. Nöfn og Hæð")
    print("2. Ekrur")
    print("3. Meiri Ekrur")
    print("4. Skammstöfun")
    print("5. Prósentur")
    print("6. Hætta")
    val=input("Veldu 1-6 eða 7 til að hætta ")
    if val=="1":
        nafn1=input("Fyrra nafn ")
        haed1=int(input("Hæð í sentimetrum "))
        nafn2=input("Seinna nafn ")
        haed2=int(input("Hæð í sentimetrum "))
        if haed1 > haed2:
            print(nafn1,"er stærri en",nafn2)
        elif haed2 > haed1:
            print(nafn2,"er stærri en",nafn1)
        else:
            print(nafn1,"og",nafn2,"eru jafnhá/ir")
    elif val=="2":
        lengd=int(input("Lengd í metrum "))
        breidd=int(input("Briedd í metrum "))
        ekrur=(lengd*breidd)/4046
        print("Þessi reitur er",round(ekrur,3),"ekrur")
    elif val=="3":
        breidd=int(input("Breidd fernings í metrum: "))
        print("Stærð\tLengd í ekrum")
        for x in range(10,101,10):
            lengd= (x*breidd)/4046
            print(x,"\t",round(lengd,6))
    elif val=="4":
        afangi=input("Skammstöfun áfanga: ")
        if len(afangi)==7:
            fyrstu3=afangi[0:3]
            sidustu4=afangi[3:]
            if fyrstu3.isalpha()==True and fyrstu3.isupper()==True and sidustu4.isdigit()==True:
                print("Þetta er rétt skammstöfun á áfanga")
            else:
                print("Þetta er ekki rétt skammstöfun á áfanga")
        else:
            print("Þetta er ekki rétt skammstöfun á áfanga")
    elif val=="5":
        heild=int(input("Hver er heildin? "))
        percent=int(input("Hver er %? "))
        nullsmth=percent/100
        result=heild*nullsmth
        print("Niðurstaðan:",result)
    elif val=="6":
        print("Ókei bæ")
    else:
        print("Rangur Innsláttur")
        
    
