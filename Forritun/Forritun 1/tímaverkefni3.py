#Höfundur Einar Karl
#Tímaverkefni 3. 21/11/2018
val=" "
import random
while val!="4":
#Valmynd
      print("1. Skrifa út tölurnar 10-99 í eina línu ")
      print("2. Vinna með tilviljanakenndar (random) tölur í lista ")
      print("3. Vinna með kennitölu")
      print("4. Hætta")
      val=input("Veldu 1-3 eða 4 til að hætta ")
      if val=="1":
            for x in range(10,100):
                  print(x,end=":")#prentar allar tölur frá 10 upp í 99 og setur : á milli
            print()
      elif val=="2":
            randomlisti=[] #bý til tóman lista
            for x in range(300):
                  tala=random.randint(170,699) #Tekur 300 handahófskenndar tölur á bilinu 170-699
                  randomlisti.append(tala)
            print(randomlisti)
            medaltal=float(sum(randomlisti)/len(randomlisti))
            print("Meðaltal talna",round(medaltal,3)) #Finnur meðaltal og endar með þrjár aukatölur
            tel=0 #Skilgreini teljara
            for tala in randomlisti:
                  if tala==210:
                        tel=tel+1 #bæti við einum í teljara ef talan 210 kemur fyrir
            print("Talan 210 er í listanum",tel,"skipti")
            fjogurh=0#skilgreini fjögurhundrað til að finna það
            for tala in randomlisti:
                  if tala >= 400:
                        fjogurh=fjogurh+tala #bætir við tölu sem er stærri en 400 í hvert sinn (fæ þannig summu)
            print("Summa talna yfir 400 er",fjogurh)
      elif val=="3":
            tel=0 #skilgreini teljara
            kennitala=input("Sláðu inn kennitölu: ")
            for tala in kennitala:
                  if tala=="1":#Finnur töluna einn 
                        tel=tel+1
            print("Fjöldi 1 er:",tel)
            print("Kennitala án 1:",kennitala.replace("1","#"))#setur # í stað fyrir 1
            print("Afmælisdagur",kennitala[0:2]+"."+kennitala[2:4]) #setur punkt á milli fyrstu fjóra
      elif val=="4":
            print("Ókei bæ")
      else:
            print("Rangur Innsláttur") #Kemur bara ef eitthvað annað en 1,2,3 eða 4 var skrifað
            
