#Einar Karl P
#29.01.2019

def brandari():
    print("Hvað heitir kranamálastjóri Japans? Svar: Hífaslaka")

def brandarar(nr):
    if nr==1:
        print("Brandari 1")
        print("funni joke")
    elif nr==2:
        print("Brandari 2")
        print("??")
    elif nr==3:
        print("Brandari 3")
        print("ye")
    else:
        print("Ekki rétt nr valið")
def finnaKyn(val):
    if val=="kk":
        print("Þú ert karlmaður")
    elif val=="kvk":
        print("Þú ert kvenmaður")
    else:
        print("Þetta kyn þekki ég ekki")

#Kalla á fall úr dæmi 1
brandari()
#Kalla á fall úr dæmi 2
numer=int(input("Veldu brandara 1 2 eða 3 "))
brandarar(numer)
#Kalla á fall úr dæmi 3
kyn=input("Hvaða kyn ert þú, kk eða kvk? ")
finnaKyn(kyn)