#Höfundur Einar Karl
import random
val=" "
while val !="5": #Valmynd
      print("--------------------------------------")
      print("1. Random Tölur")
      print("2. Talnabil")
      print("3. Strengjalisti")
      print("4. Samanburður")
      print("5. Hætta")
      val=input("Veldu 1-4 eða 5 til að hætta ")
      if val=="1":
            randomlisti=[]
            for x in range(50):
                  tala=random.randint(5,70)#tekur 50 tölur á bilinu 5-70
                  randomlisti.append(tala)
            margfald=1
            for tala in randomlisti:
                  margfald=margfald*tala#margfaldar tölunum
            #útskrift
            print("Margfeldi alla talnanna er",margfald)
            print("Hæðsta talan er = ",max(randomlisti))
            print("Lægsta talan er = ",min(randomlisti))
            print("Óraðaður")
            print(randomlisti)
            print("Raðaður")
            randomlisti.sort()
            print(randomlisti)
            
                  
      elif val=="2":
            listi_7=[] #skilgreini listann
            for tala in range(2000,3201):
                  if tala % 7==0 and tala % 5!=0: #ef talan 7 gengur upp i þessa tölu
                        listi_7.append(tala)
            print(listi_7)
            samtala=sum(listi_7)
            print("Summa talnanna er",samtala)
      elif val=="3":
            nofn=[]
            for x in range(10):
                  nafn=input("Sláðu inn nafn númer "+str(x+1)+" ")
                  nofn.append(nafn)
            print(nofn)
            tel=1
            print("Nöfn með fjórum stöfum eru: ")
            for nafn in nofn:
                  if len(nafn)==4: #finn öll orð sem eru fjórir stafir
                        print(nafn)
            print("Annað hvert orð öfugt:")
            for nafn in nofn:
                  if tel % 2 !=0:#oddatala
                        print(nafn[::-1])#sný nafninu við
                  else:
                        print(nafn)
                  tel+=1
            nofn.sort()
            print("Raðað í stafrófsröð: ",nofn)
            stafur=str(input("Sláðu inn staf sem eyðir orðum sem byrja á honum "))
            for nafn in nofn:
                  if nafn[0]==(str(stafur)):
                        nofn.remove(nafn)
            print(nofn)
      elif val=="4":
            listar1=[]
            listar2=[]
            for x in range(7):
                  nafn=input("Sláðu inn orð númer "+str(x+1)+" ")
                  listar1.append(nafn)
            print(listar1)
            for x in range(6):
                  nafn=input("Sláðu inn orð númer "+str(x+1)+" ")
                  listar2.append(nafn)
            print(listar2)
            listisama=[]
            for nafn in listar1:
                  if nafn in listar2:
                        listisama.append(nafn)
            print("Orðin sem eru eins eru",listisama)
      elif val=="5":
            print("Ókei bæ")
      else:
            print("Rangur Innsláttur")
