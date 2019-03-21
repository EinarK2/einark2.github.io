#Höfundur Einar Karl
#Dagsetning 5/3/2019 og 12/3/2019
#Föll:
#1:
def nyrListi():
    listi=[] # Skilgreinir lista
    for x in range(2,1001,2): # Keyrir aðrahvora tölu frá 2-1000(sléttartölur)
        listi.append(x) #Setur í lista
    return listi #Skilar Listanum
def skrifaiSkra(listi, nafntxt):
    skra = open(nafntxt,"w",encoding="utf-8") # Opnar skrá
    for x in listi: # Fer í gegnum lista
        skra.write(str(x)+" ") #Skrifar í skrá með bili
    skra.close() #lokar skránni
def lesaSkra(nafnTxtSkra):
    skra = open(nafnTxtSkra,"r",encoding="utf-8") #opnar skrá
    listi = (skra.read().split(' ')) #Les innihald án bila
    skra.close() #Lokar skrá
    listi.pop() #Tekur síðasta í lista
    listi = list(map(int,listi))# Breytir lista svo innihald hans er int
    return listi #Skilar lista
def prenta(listi):
    for x in listi:  # Fer í gegnum lista
        print(x)   # Prentar allt í honum
def medaltal(listi):
    medaltal = float(sum(listi) / len(listi)) #Finnur meðaltal lista
    return round(medaltal,2) #Skilar meðaltali með 2 aukastafi
def attan(listi):
    l=[] #Skilgreini lista
    for x in listi:     #Fer í gegnum lista
        if x % 8==0:    #Ef tala gengur upp í átta
            l.append(x) #Setur í lista
    return l #Skilar lista
def prenta10(listi):
    for x in range(len(listi)): #Fer í gegnum len af lista
        if x%10==0 and x != 0: #þegar 10 kemur skiptir um línu (fyrir neðan)
            print(listi[x]) #Prentar tölu
        else:  # Til að skipta um línu
            print(listi[x], end="\t")
#2:
def primListi():
    listi = [] #Skilgreini lista
    for x in range(1,101): #keyrir frá 1 upp í 101
        if x > 1: # Til að gá hvort talan er prímtala
            for i in range(2, x):
                if (x % i) == 0:
                    break
            else:
                listi.append(x) #Setur prímtölu í lista
    return listi # Skilar listanum
def sjo(listi):
    listi = list(map(str, listi)) #Breytir lista í string
    for x in listi: #Fer í gegnum lista
        if '7' in x: #Ef 7 er í tölunni
            print(x) #Prentar tölu
def fjorda(listi):
    return listi[::4] #Skilar listanum með fjórða hverja tölu
#3:
def skrifaTupleSkra(tup, nafntxt):
    skra = open(nafntxt, "a+", encoding="utf-8") #Opna skrá með a+
    skra.write(str(tup)) #Skrifa tuple
    skra.write("\n") #Enter
    skra.close() #Loka skrá
def lesaTupSkra(nafnTxtSkra):
    skra = open(nafnTxtSkra, "r", encoding="utf-8") #Opna skrá
    print(skra.read()) #Les (prenta)
    skra.close()#loka
def buaTilTuple():
    oft=int(input("Hve mikið viltu setja í tuple-ið? "))
    tel=1 #Skilgreini teljara
    l=[] #Skilgreini lista
    for x in range(oft): #Fer í gegnum hve oft var beðið um
        t=str(input("Sláðu inn tuple "+str(tel)+": ")) #Biður um streng
        l.append(t) #Setur hann í lista
        tel +=1 #Bætir við á teljaran
    tup=tuple(l) #Breyti listanum í tuple
    return tup #skila tuple
def summaTuple(nafnTxtSkra):
    skra = open(nafnTxtSkra, "r", encoding="utf-8") #Opna skra
    skra.seek(0) #Leita að fyrstu línu
    listi=list(map(int, skra.readline()[1:-2].split(", "))) #Geri int lista sem les fyrstu línu og tekur út kommur og bil og sviga
    skra.close()  #Loka skrá
    return sum(listi) #Skila summu listans
#4:
def nyttDict():
    oft = int(input("Hve mikið viltu setja í dict-ið? "))
    dict = {} #Skilgreini dict
    for x in range(oft): #keyrir eins oft og beðið var um
        dict[input("Nafn : ")] = input("Tala : ") #Gerir dict og gerir input fyrir hvert key og value
    return dict #Skilar dict
def skrifaDict(dict, nafntxt):
    skra = open(nafntxt,"a+",encoding="utf-8") #Opna Skrá
    skra.write(str(dict)) #Skrifa dict í skránna
    skra.write("\n") #Enter
    skra.close() #Loka skránni
def lesaDict(nafnTxtSkra):
    skra = open(nafnTxtSkra,"r",encoding="utf-8") #Opna skrá
    print(skra.read()) #Prenta innihald skránna
    skra.close() #Loka skrá
def prentaDict(nafnTxtSkra):
    skra = open(nafnTxtSkra, 'r', encoding='utf-8') #Opna Skrá
    for teljari, x in enumerate(skra): #Fer í gegnum skrá
        print("Lína", teljari + 1, ":") #Prentar fyrir hverja línu
        listi = x[1:-2].split(", ") #Tekur slaufusviga og kommur út
        for i in listi: #Fer í gegnum lista
            strengur = i.replace("'", "") # tekur ' út
            lykill, gildi = strengur.split(":") #Tekur : út
            print(lykill + " ", gildi) #Skrifar lykil og gildi
    skra.close()
#tuple:
tolur=(1,2,3,4,5,6,7,8,9)
stafir=('a','b','c','d','e','f','g','h')
nafn=("konni",123,"sponni",234)
#Valmynd:
val=" "
while val !="5":
    print("1. Sléttar Tölur")
    print("2. Prímtölur")
    print("3. Tuple Skrá")
    print("4. Dictionary")
    print("5. Hætta")
    val=input("Veldu 1-4 eða 5 til að hætta ")
    if val=="1":
        listi = nyrListi()
        skrifaiSkra(listi, "slettartolur")
        listi2 = lesaSkra("slettartolur")
        print("Allur listinn:")
        prenta(listi2)
        print("Meðaltal: ")
        print(medaltal(listi2))
        attaListi=attan(listi2)
        skrifaiSkra(attaListi, "sumarslettartolur")
        print("Listinn með 10 tölur í línu:")
        prenta10(listi2)
        print() #Bil
    elif val=="2":
        primtolur = primListi()
        skrifaiSkra(primtolur, "primtolur")
        listi=lesaSkra("primtolur")
        print("Allur listinn:")
        prenta(listi)
        print("Allar tölur sem innihalda 7:")
        sjo(primtolur)
        print("Listinn með fjórða hverja tölu:")
        fjordaListi=fjorda(primtolur)
        print(fjordaListi)
        skrifaiSkra(fjordaListi,"fjorda")
    elif val=="3":
        print("Tuple-ið:")
        skrifaTupleSkra(tolur,"tuple")
        skrifaTupleSkra(stafir,"tuple")
        skrifaTupleSkra(nafn,"tuple")
        lesaTupSkra("tuple")
        nyttTuple=buaTilTuple()
        print(nyttTuple)
        skrifaTupleSkra(nyttTuple,"tuple")
        print("Summa talnanna í fyrsta tuple-inu er:",summaTuple("tuple"))
    elif val=="4":
        dict1=nyttDict()
        skrifaDict(dict1,"dictskra")
        lesaDict("dictskra")
        dict2=nyttDict()
        skrifaDict(dict2,"dictskra")
        dict3=nyttDict()
        skrifaDict(dict3,"dictskra")
        prentaDict("dictskra")
    elif val=="5":
        print("Ókei Bæ")
    else:
        print("Rangur Innsláttur")
