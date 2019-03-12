#Höfundur Einar Karl Pétursson
#Dagsetning 15/2/2019

#Valmynd
val=""
while val!="4":
    print("")
    print("1. Bæta í skrána")
    print("2. Birta skrána í heild sinni")
    print("3. Birta upplýsingar um ákveðið dýr eftir nafni ")
    print("4. Hætta")
    val=input("Veldu 1-3 eða 4 til að hætta: ")
    if val=="1":
        nafn = input("Sláðu inn nafn eiganda: ")
        dyr = input("Sláðu inn nafn gæludýrs: ")
        tegund = input("Sláðu inn tegund gæludýrs: ")
        with open("Timaverkefni.txt", 'a', encoding='utf-8') as f:  # Opnar skránna og skrifar eftirfarandi í hana
            f.write(nafn + ";")
            f.write(dyr + ";")
            f.write(tegund + "\n")  # /n til að skipta um línu
            f.close()  # Lokar skránni
    elif val=="2":
        print("Eigandi: Dýr:\tTegund:")
        f = open("Timaverkefni.txt", 'r', encoding='utf-8')
        for x in f:
            lina = x.split(";")
            tegund = lina[2].replace("\n", "")
            dyr = lina[1]
            print(lina[0] + "  \t" + dyr + " \t" + tegund)
    elif val=="3":
        dyr=input("Sláðu inn nafn á dýri: ")
        f = open("Timaverkefni.txt", 'r+', encoding='utf-8')
        allir = []
        for line in f:
            lina = line.split(";")
            allir.append(lina)
        f.close()
        listi=[]
        for i in allir:
            if i[1]==dyr:
                for x in i:
                    listi.append(x)
        print("Eigandi: Dýr:\tTegund:")
        for x in listi:
            print(x, end=" \t")
    elif val=="4":
        print("Ókei bæ")
    else:
        print("Rangur Innsláttur")