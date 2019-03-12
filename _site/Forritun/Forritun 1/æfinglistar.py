#Æfingaverkefni
val=" "
import random
while val!="5":
      print("1. Innkaupalisti")
      print("2. Randomtölur")
      print("3. Fyrsta og síðasta")
      print("4. Nemendur")
      print("5. Hætta")
      val=input("Veldu 1-4 eða 5 til að hætta ")
      if val=="1":
            innkaupalisti=[]#bý til tóman lista
            svar="j"
            while svar=="j":
                  vara=input("Sláðu inn vöru ")
                  innkaupalisti.append(vara) #set vöru inn í innkaupalista
                  svar=input("Viltu bæta við vöru (j/n) ").lower()
            print("Þetta er listinn í stafrófsröð")
            innkaupalisti.sort() # raða listanum í stafrófsröð
            print(innkaupalisti)
            
      elif val=="2":
            randomlisti=[] #skilgreini lista
            for x in range(15): #keyrir 15 sinnum
                  tala=random.randint(5,25)
                  randomlisti.append(tala)
            #fer út úr forslaufunni
            print("Listinn raðaður")
            randomlisti.sort() #raða listanum eftir stærð minnsta talan fyrst
            print(randomlisti)
            print("Hæðsta talan",max(randomlisti))
            print("Lægsta talan",min(randomlisti))
            print("Summa talnanna er",sum(randomlisti))
            print("Fjöldi talna í listanum er",len(randomlisti))
            medaltal=sum(randomlisti)/len(randomlisti)
            print("Meðaltal talna",round(medaltal,2))
            
            
      elif val=="3":
            randomlisti2=[] #skilgreini lista
            nyrlisti=[]
            for x in range(20): #keyrir 20 sinnum
                  tala=random.randint(1,200)
                  randomlisti2.append(tala)
            nyrlisti.append(randomlisti2[0]) #fyrsta talan
            nyrlisti.append(randomlisti2[-1]) #bæti síðustu tölunni við
            print("Randomlistinn")
            print(randomlisti2)
            print("Listinn með fyrstu og síðustu tölunum")
            print(nyrlisti)
      elif val=="4":
            nafnalisti=[]
            teljari=0
            while teljari < 10: 
                  nafn=input("Sláðu inn nafn númer "+str(teljari+1)+" ")
                  if nafn in nafnalisti: #ef nafnið er í listanum
                        teljari=teljari-1
                  else:
                        nafnalisti.append(nafn)
                  teljari=teljari+1 #bæti einum við teljara
            #kominn út úr forslaufunni
            nafnalisti.reverse()
            print(nafnalisti)
                  
      elif val=="5":
            print("Ókei bæ")
      else:
            print("Rangur Innsláttur")
