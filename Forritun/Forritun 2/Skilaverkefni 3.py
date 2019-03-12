#Höfundur Einar Karl
#Dags. 21/2/2019
import random
#Def
#1:
def prentaTuple(tup):
    for x in tup:#Fer í gegnum tuple
        print(x, end=" ")#og prentar innihaldið(x) með bili á milli
def paraRod(tup1, tup2):
    for x in range(len(tup1)):#Keyrir í gegnum tuple eins og oft og len af því er
        print(tup1[x],"og",tup2[x]) #Prentar tuple1 og tuple2 í hvert sinn
def paraRandom(tup1, tup2):
    for x in range(len(tup1)):#Keyrir í gegnum tuple eins og oft og len af því er
        print(random.choice(tup1),"og",random.choice(tup2))#Prentar random úr tuple 1 og 2 saman
def paraRandomStakur(tup1, tup2):
    t1=list(range(len(tup1)))#Gerir lista af len úr tuple1
    for x in range(len(t1)):#Keyrir í gegnum listan eins og oft og len af því er
        print(tup1[x],"og",tup2[x])#Prentar x úr tup 1 og 2
def finnaNafn(stafur, tup):
    l=[] #Skilgreini lista
    for x in tup: #Fer í gegnum tup
        if x.count(stafur):#Ef stafur er í tup
            l.append(x) #Setur x í listan
    return l #Skilar listanum
def fyrstiStafur(stafur, tup):
    l=[] #Skilgreinir lista
    for x in tup: #Fer í gegnum tup
        if x[0]==stafur: #Ef fyrsti stafurinn er sami og stafur:
                l.append(x) #Setur x í listann
    return l #Skilar listanum
def finnaN(tup1, tup2):
    l=[] #Skilgreinir lista
    for x in tup1: #Fer í gegnum tup1
        if x.count("n")>1: #ef stafurinn 'n' er :
            l.append(x) #Setur x í lista
    for x in tup2:#Sama nema í tup2 en setur í sama lista
        if x.count("n")>1:
            l.append(x)
    return l #Skilar listanum
#2:
def dictNafn(nafn, dict):
    if nafn in dict: #Ef nafn er í dict:
        print("Símanúmerið er:",dict.get(nafn)) #Prentar símanúmerið
    else: #Skilar þessu frá sér ef nafnið er ekki í dict
        print("Þetta nafn er ekki til í skránni")
#3:
def prentaDict(dict):
    print("Allir nemendur:")#Prentar þetta
    for x in dict: #Fer í gegnum dict
        print(x,"--------",dict[x]) #Prentar key(x) og value(dict[x])
def dict18(dict):
    listi=[] #Skilgreinir lista
    print("Allir nemendur sem eru orðnir 18:") #Prentar þetta
    for x in dict: #Fer í gegnum dict
        if dict[x] >= 18: #Ef gildi er meira eða jafnt og 18:
            listi.append(dict[x]) #Setur gildi í listann
            print(x, "--------", dict[x]) #Prentar key(x) og value(dict[x])
    print("Fjöldi nemenda sem eru orðnir 18 er",len(listi)) #Prentar þetta með fjölda listans (len)
def medalDict(dict):
    listi=[] #Skilgreinir lista
    for x in dict: #Fer í gegnum dict
        listi.append(dict[x]) #Setur gildi í lista
    medaltal=float(sum(listi)/len(listi)) #Reiknar meðaltal gildana með listanum
    print("Meðalaldur bekkjarins er:",round(medaltal,2)) #Sýnir meðalaldur með 2 aukastöfum
def heildDict(dict):
    listi=[] #Skilgreinir lista
    for x in dict: #Fer í gegnum dict
        listi.append(dict[x])#Setur gildin í listann
    print("Heildaraldur allra í bekknum er:",sum(listi)) #Finnur summu listans (gildana)
def stafurDict(stafur, dict):
    l=[]#Skilgreinir lista
    for x in dict: #Fer í gegnum dict
        if x[0]==stafur:#Ef fyrsti stafurinn er sá sami og stafur:
            print(x, "--------", dict[x]) #Prentar key(x) og value(dict[x])
            l.append(dict[x])#Setur gildið í listann
    return l #Skilar listanum
def medalDictStafur(l):
    medaltal = float(sum(l) / len(l))#Reiknar meðaltal af lista
    return round(medaltal, 2) #Skilar meðaltalinu með 2 aukastöfum
#Tuple:
herraTuple=("Jón","Jóngeir","Arnar","Halli","Gunnar","Gústi")
domuTuple=("Jónína","Jónun","Arna","Halla","Gunna","Gústa")
#Valmynd:
val=" "
while val !="4":
    print("1. Danspörin")
    print("2. Símaskrá")
    print("3. Skráning í bekk")
    print("4. Hætta")
    val=input("Veldu 1-3 eða 4 til að hætta ")
    if val=="1":
        print("Herra tuple er:")
        prentaTuple(herraTuple)
        print()#Vantaði bil
        print("Dömu tuple er:")
        prentaTuple(domuTuple)
        print("") #Vantaði annað bil
        print("Pöruð saman í röð:")
        paraRod(herraTuple, domuTuple)
        print("Pöruð saman af handahófi:")
        paraRandom(herraTuple, domuTuple)
        kk=random.sample(herraTuple,len(herraTuple)) #Tekur random úr tuple en tekur ekki sama aftur
        kvk=random.sample(domuTuple,len(domuTuple)) #Sama og uppi
        print("Pöruð af handahófi en stakt:")
        paraRandomStakur(kk,kvk)
        stafur=input("Sláðu inn staf: ")
        print("Hér eru herra nöfn með stafnum",stafur+":",finnaNafn(stafur, herraTuple))
        print("Hér eru dömu nöfn með stafnum",stafur+":",finnaNafn(stafur, domuTuple))
        fyrsti=input("Sláðu inn fyrsta staf: ")
        print("Hér eru herra nöfn með stafnum",fyrsti,"sem fyrsta staf:",fyrstiStafur(fyrsti,herraTuple))
        print("Hér eru dömu nöfn með stafnum",fyrsti, "sem fyrsta staf:", fyrstiStafur(fyrsti, domuTuple))
        print("Nöfn sem eru með meira en eitt n:",finnaN(herraTuple, domuTuple))
    elif val=="2":
        dict = {'Einar Karl':6948820,'Guðmundur':8411350,'Geir':6117573, 'Gabríel':8552428,'Róbert':8210601,'Brynjar':6960925,'Trausti':8416950,'Gabríel Elí':8441477,'Eydís':6643103,'Pétur':8992307}
        nafn = input("Sláðu inn nafn ")
        dictNafn(nafn, dict)
    elif val=="3":
        bekkjaDict={'Einar':16,'Gummi':16,'Jónas':19,'Jens':18,'Jóngeir':19,'Brynjar':17,'Trausti':18,'Róbert':17,'Geir':16,'Gabríel':17,'Dagný':16,'Guðrún':20,'Sigríður':21,'Líney':15,'Eydís':21}
        prentaDict(bekkjaDict)
        dict18(bekkjaDict)
        medalDict(bekkjaDict)
        heildDict(bekkjaDict)
        stafur=input("Sláðu inn staf ")
        listi=(stafurDict(stafur, bekkjaDict))
        print("Meðaldur þeirra er: ",medalDictStafur(listi))
    elif val=="4":
        print("Ókei bæ")
    else:
        print("Rangur Innsláttur")