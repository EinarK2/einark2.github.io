#Einar Karl P
#29.01.2019

#Deffffffff:
def skrifaUt(listi):
    return listi
def staersta(listi):
    staersta = listi[0]
    for x in listi:
        if x > staersta:
            staersta = x
    return staersta
def minnsta(listi):
    minnsta=listi[0]
    for x in listi:
        if x < minnsta:
            minnsta = x
    return minnsta
def summa(listi):
    summa=0
    for x in listi:
        summa = summa + x
    return summa
def medaltal(listi):
    summa = 0
    for x in listi:
        summa = summa + x
    fjoldi = 0
    for i in listi:
        fjoldi = fjoldi+1
    medaltal=summa/fjoldi
    return medaltal

def setning(fyrsta='Hér',annad='er',tridja='smá',fjorda='texti'):
    print(fyrsta,annad,tridja,fjorda)

def medaltal2(*tolur):
    summa=0
    for tala in tolur:
        summa = summa + tala
    fjoldi = 0
    for tala in tolur:
        fjoldi = fjoldi + 1
    medaltal2 = summa / fjoldi
    print(round(medaltal2,3))

def finnaord(texti,ord):
    if ord in texti:
        print("Orðið er í textanum ")
    else:
        print("Orðið er ekki í textanum")

#Valmynd
val=""
while val!=5:
    print("1. Talnalisti")
    print("2. Sjálfgefin gildi")
    print("3. Ótilgreindur fjöldi breyta")
    print("4. Finna orð")
    print("5. Hætta")
    val=int(input("Veldu "))
    if val==1:
        listi=[]
        for x in range(5):
            tala=int(input("Sláðu inn tölu númer "+str(x+1)+" "))
            listi.append(tala)
        print(skrifaUt(listi))
        print(staersta(listi))
        print(minnsta(listi))
        print(summa(listi))
        print(medaltal(listi))
    elif val==2:
        setning()
        setning("Hvar")
        setning("Hvar","var")
        setning("Hvar","var","þessi")
        setning("Hvar", "var", "þessi","api")
    elif val==3:
        medaltal2(1,53,32,543,12,432)
        medaltal2(1,25,00)
        medaltal2(1,2,3,4)
        medaltal2(1)
    elif val==4:
        texti=input("Sláðu inn texta ")
        ord=input("Sláðu inn orð til að gá hvort það er í textanum ")
        finnaord(texti,ord)
    elif val==5:
        print("Ókei bæ")
    else:
        print("Rangur innsláttur")