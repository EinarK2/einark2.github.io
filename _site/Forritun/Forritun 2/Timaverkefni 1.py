#Höfundur Einar Karl Pétursson
#14/2/2019
#Import:
import random
#Def:
def randomListi(byrjun, endir, fjoldi):
    listi=[]
    for x in range(fjoldi): #Forlúppa sem keyrir "Fjoldi" sinnum
        tala= random.randint(byrjun,endir)#gefur random tölur á bilinu "byrjun"-"endir" og
        listi.append(tala) #setur í lista
    return listi #skilar listanum
def einsTolur(l1,l2):
    l3=[]
    for i in l1: #Tekur lista og finnur tölur sem eru eins í öðrum lista
        for a in l2:
            if i == a:
                l3.append(i) #Og setur svo í þrðja listan
    return l3 #Skilar listanum
def ofugt(texti):
    if len(texti) <= 1:
        return texti
    return ofugt(texti[1:]) + texti[0] #Skilar textanum öfugum
def reiknaGroda(soluv, innkv, vsk):
    agodi=(soluv-(innkv+vsk)) #Reiknar ágóða
    return agodi #Skilar ágóða
def prenta(agodi):
    if agodi > 0: #Ef ágóðinn er venjuleg tala
        print("Ágóðinn er:", agodi)
    elif agodi==0: #Ef ágóðinn er 0
        print("Hækkaðu álagninguna á vörunni þinni.")
    else: #Ef ágóðinn er mínus tala
        print("Hér hefur eitthvað farið úrskeiðis..")
#Valmynd:
val=" "
while val !="4":
    print("1. Listi")
    print("2. Strengur")
    print("3. Föll")
    print("4. Hætta")
    val=input("Veldu 1-3 eða 4 til að hætta ")
    if val=="1":
        l1=randomListi(50, 100, 100)
        l2=randomListi(75, 200, 150)
        print("Listi A:")
        for x in range(1,len(l1)): #Lúppa sem aðskilur allar tölurnar (4 tölur í línu
            if x%9==0: #Prentar þangað til að fjórar tölur eru komnar
                print(l1[x])
            else:  # Til að skipta um línu
                print(l1[x], end="\t")
        print("Listi B:")
        for x in range(1,len(l2)):
            if x%15==0:
                print(l2[x])
            else:  # Til að skipta um línu
                print(l2[x], end="\t")
        print("")
        l3=einsTolur(l1, l2)
        print("Tölurnar sem eru eins úr lista A og B eru:")
        for x in range(1,len(l3)):
            if x%9==0:
                print(l3[x])
            else:  # Til að skipta um línu
                print(l3[x], end="\t")
        print("")
    elif val=="2":
        texti=input("Sláðu inn texta ")
        print("Fjöldi orða í textanum eru:", len(texti.split())) #Finnur fjölda orða í texta
        print("Lengd strengsins er:",len(texti)) #Finnur lengd textans
        x=texti.count("B")
        y=texti.count("b")
        print("Fjöldi b/B í textanum er:",x+y) #Hér skilgreini ég x og y sem telur B/b og set töluna samanlagða hér
        numer = sum(c.isdigit() for c in texti)#Finnur númer í textanum
        print("Fjöldi talna í strengum er:",numer)
        print("Textinn öfugur:",ofugt(texti))

    elif val=="3":
        innkv=int(input("Sláðu inn innkaupsverð: "))
        vsk=int(input("Sláðu inn virðisaukaskatt: "))
        soluv=int(input("Sláðu inn söluverð: "))
        agodi=reiknaGroda(soluv,innkv,vsk)
        prenta(agodi)
    elif val=="4":
        print("Ókei bæ")
    else:
        print("Rangur Innsláttur") #Ef sláð er inn annað en beðið var um