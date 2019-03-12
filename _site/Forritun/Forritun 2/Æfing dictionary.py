#Höfundur Einar Karl Pétursson
#Dagsetning 19/2/2019

#Def:
def geraDict():
    mDict={1:"Gulur",2:"Rauður",3:"Grænn",4:"Blár",5:"Svartur",6:"Hvítur",7:"Fjólublár",8:"Brúnn",9:"Bleikur",10:"Appelsínugulur"}
    return mDict
def prentaDict(dict):
    for x in dict:
        print("Númer",x,"er",dict[x])
def eydalit(keyNr,dict):
    dict.pop(keyNr)
    return dict
def prentaLit(keyNr, dict):
    print(dict.get(keyNr))
def nyrDict(staerd):
    #dict2 = {value: key for (key, value) in dict.items()}
    #print(dict2)
    myDict={}
    for x in range(1,staerd+1):
        nafn=input("Sláðu inn nafn")
        temp={x:nafn}
        myDict.update(temp)
    return myDict
#Valmynd:
litaDict={}
val=""
while val != "8":
    print("1. Búa til dictionary")
    print("2. Prenta dictionary")
    print("3. Eyða lit")
    print("4. Prenta ákveðin lit")
    print("5. Gera afrit af dict – eyða dict og prenta síðan bæði")
    print("6. Sýna notkun fallanna items(), keys(), values() og clear()")
    print("7. Gerðu fall sem býr til nýtt dictionary með tölum sem lykli/key og nöfnum sem gildi/value.")
    print("8. Hætta")
    val = input("Veldu 1-7 eða 8 til að hætta ")
    if val == "1":
        litaDict = geraDict()
    elif val == "2":
        prentaDict(litaDict)
    elif val == "3":
        keyNr=int(input("Veldu númer lits til að eyða: "))
        eydalit(keyNr,litaDict)
    elif val == "4":
        keyNr=int(input("Veldu númer lits til að sýna: "))
        prentaLit(keyNr, litaDict)
    elif val == "5":
        nyttDict = litaDict.copy()
        print(nyttDict)
        nyttDict.clear()
        print(nyttDict)
        del(nyttDict)
        #print(nyttDict)
    elif val == "6":
        print("items():")
        print(litaDict.items())
        print("keys():")
        print(litaDict.keys())
        print("values():")
        print(litaDict.values())
        print("Og clear() sem eyddi dict inu")
        litaDict.clear()
    elif val == "7":
        staerd=int(input("Sláðu inn stærð "))
        nyrDict(staerd)
    elif val=="8":
        print("Ókei bæ")
    else:
        print("Rangur Innsláttur")
