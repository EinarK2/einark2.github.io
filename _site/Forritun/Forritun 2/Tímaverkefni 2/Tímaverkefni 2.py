#Höfundur Einar Karl Pétursson
#Dagsetning 3.14.2019 !

#Föll:
#1:
def lesaSkra(nafnTxt):
    skra = open(nafnTxt,"r",encoding="utf-8")
    listi = (skra.read().split(','))
    skra.close()
    listi = list(map(int,listi))
    for x, y in enumerate(listi, 1):
        if x % 3 == 0:
            print(y)
        else:
            print(y, end=" ")
def summaFimm(nafnTxt):
    skra = open(nafnTxt, "r", encoding="utf-8")
    listi = (skra.read().split(','))
    skra.close()
    l=[]
    for x in listi:
        if x[0]=='5':
            l.append(x)
    l = list(map(int, l))
    return sum(l)
#2:
def prentaTuple(tup):
    tel=1
    for x in tup:
        print(str(tel)+"=>",x)
        tel+=1
#3:
def medaltalStafa(dict,listi):
    for x in dict:
        listi.append(x)
    medaltal = float(sum(listi) / len(listi))
    return round(medaltal, 2)
def tolurNafn(dict,str):
    l=[]
    str = str.replace(";", " ")
    strList=str.split()
    #print(strList)  gefst upp
    for x in strList:
        if x in dict:
            print(dict[x], end=" ")
            l.append(dict[x])
    return l
#Tuple:
fiskiTuple=('veiðistöng', 'fluga', 'veiðihjól', 'stígvél', 'taska', 'háfur')
#Dict:
stafrofsDict = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k'}
#Valmynd:
val=""
while val != "4":
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. Hætta ")
    val=input("Veldu 1-3 eða 4 til að hætta ")
    if val=="1":
        lesaSkra("skr.txt")
        print("Summa talna sem byrja á fimm:")
        print(summaFimm("skr.txt"))
    elif val=="2":
        prentaTuple(fiskiTuple)
        stafur=input("Sláðu inn staf: ")
        for x in fiskiTuple:
            if x[0]==stafur:
                print(x, end=" ")
        print()
    elif val=="3":
        listi=[]
        print("Meðaltal talna í dict er:")
        print(medaltalStafa(stafrofsDict,listi))
        print(tolurNafn(stafrofsDict,"10;14;13;13;8"))
    elif val=="4":
        print("Ókei bæ")
    else:
        print("Rangur Innsláttur")