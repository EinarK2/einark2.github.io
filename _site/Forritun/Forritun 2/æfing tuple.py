#Höfundur Einar Karl
#Dags. 19/2/2019



#Valmynd:
val=" "
while val !="6":
    print("1. Tuple með sex stökum")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. ")
    print("6. Hætta")
    val=input("Veldu 1-5 eða 6 til að hætta ")
    if val=="1":
        myTuple=(1,2,3,"MIKIÐ","GAMAN","NÚNA")
        print(myTuple)
        print(myTuple[2])
        for x in myTuple:
            print(x,end= ":")
    elif val=="2":
        listi1 = []
        listi2 = []
        listi3 = []
        listi4 = []
        listaTuple=(listi1,listi2,listi3,listi4)
        
    elif val=="3":
        pass
    elif val=="4":
        pass
    elif val=="5":
        pass
    elif val=="6":
        pass