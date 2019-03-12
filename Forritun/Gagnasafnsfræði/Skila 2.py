#Höfundur Einar Karl

val=" "
while val !="5":
    print("1. Bæta við nýjum í símaskrána")
    print("2. Breyta Upplýsingum í símaskránni")
    print("3. Eyða upplýsingum/eyða línu úr símaskránni")
    print("4. Prenta út alla símaskrána ein lína per notanda.")
    print("5. Hætta í forritinu ")
    val=input("Veldu 1-5: ")
    if val=="1":
        nafn=input("Sláðu inn nafn einstaklingsins: ")
        kennitala=input("Sláðu inn kennitölu einstaklingsins: ")
        simi=input("Sláðu inn símanúmer einstaklingsins: ")
        with open("simaskra.txt",'a', encoding='utf-8') as f: #Opnar skránna og skrifar eftirfarandi í hana
            f.write(nafn+";")
            f.write(kennitala+";")
            f.write(simi+"\n") #/n til að skipta um línu
            f.close() #Lokar skránni
    elif val=="2":
        kennitala=input("Sláðu inn kt þess sem þú vilt breyta: ")
        f = open("simaskra.txt", 'r+', encoding='utf-8')
        allir=[]
        for line in f:
            lina=line.split(";")
            allir.append(lina)
        f.close()
        nafn=input("Sláðu inn breytingu á nafni: ")
        simi=input("Sláðu inn annað símanúmer: ")
        teljari=0
        for i in allir:
            if i[1]==kennitala:
                allir[teljari][1] = kennitala #Uppfært
                allir[teljari][0] = nafn
                allir[teljari][2] = simi
                break;
            teljari=teljari+1

        f = open("simaskra.txt", 'a+', encoding='utf-8')
        f.seek(0)
        f.truncate()
        for x in allir:
            f.write(x[0]+";"+x[1]+";"+x[2]+"\n")
        f.close()
    elif val=="3":
        lina=int(input("Veldu línu til að eyða úr: "))
        infile = open('simaskra.txt', 'r').readlines()
        with open('simaskra.txt', 'w') as outfile:#Opnar skránna
            for index, line in enumerate(infile): #Finnur línuna sem var valin
                if index != (lina-1):
                    outfile.write(line) #Eyðir línunni
    elif val=="4":
        print("Kt:        Sími: \tNafn:")
        f = open("simaskra.txt", 'r', encoding='utf-8')
        try:#Try og except svo það kemur ekki error (keyrir samt vel)??
            for x in f:
                lina = x.split(";")
                simi = lina[2].replace("\n", "")
                kennitala=lina[1]
                print(kennitala+" "+simi+"\t"+lina[0])
        except:
            pass
        f.close()
        print()

    elif val=="5":
        print("Ókei bæ")
    else:
        print("Rangur Innsláttur")