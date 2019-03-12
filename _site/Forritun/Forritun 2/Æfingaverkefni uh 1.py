#Höfundur Einar Karl

val=" "
while val !="7":
    print("1. Tvær tölur")
    print("2. Fornafn og Eftirnafn")
    print("3. Lengd km og metrar")
    print("4. Klst og laun")
    print("5. Heildarlaun")
    print("6. Gráður")
    print("7. Hætta")
    val=input("Veldu 1-6 eða 7 til að hætta ")
    if val=="1":
        tala1=int(input("Sláðu inn tölu "))
        tala2=int(input("Sláðu inn aðra tölu "))
        print("Tölurnar lagðar saman eru",tala1+tala2)
        print("Tölurnar margfaldaðar eru",tala1*tala2)
    elif val=="2":
        fornafn=input("Fornafn? ")
        eftirnafn=input("Eftirnafn? ")
        fulltnafn=fornafn+" "+eftirnafn #hm
        print("Halló",fulltnafn.title())
    elif val=="3":
        km=float(input("Lengd í kílómetrum? "))
        metrar=km*1000
        print(km,"kílómetrar eru",metrar,"metrar")
    elif val=="4":
        laun=int(input("Laun á klukkustund? "))
        klst=int(input("Fjöldi klukkustunda sem unnið er? "))
        print("Heildarlaun verða þá:",laun*klst)
    elif val=="5":
        laun=int(input("Laun á klukkustund? "))
        klst=int(input("Fjöldi klukkustunda sem unnið er? "))
        heild=laun*klst
        print("Heildarlaun verða þá:",heild)
        if heild>30000:
            skattur=(heild-30000)*0.2
            print("Skattur",skattur,"krónur")
        if heild<30000:
            print("Skattur 0 krónur")
    elif val=="6":
        gradur=int(input("Hversu margar gráður? "))
        hringir=gradur//360
        restin=gradur%360
        print("Það eru",hringir,"og",restin,"gráður")
        
    elif val=="7":
        print("Ókei bæ")
    else:
        print("Rangur Innsláttur")
        
    
