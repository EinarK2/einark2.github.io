#Höfundur Einar Karl
import random
val=" "
#Valmynd
while val !="6":
      print("1. Stjörnuferningur")
      print("2. Craps")
      print("3. Finna Prímtölu")
      print("4. Hangman")
      print("5. Færa fremsta tölustaf aftast")
      print("6. Hætta")
      val=input("Veldu 1-5 eða 6 til að hætta ") #Biður um val
      if val=="1":
            tala=() #Skilgreini tala fyrir while loop
            while tala!=0:
                  tala=int(input("Stærð á ferning (0 til að hætta)? "))
                  tala=abs(tala)
                  for x in range(tala): #Keyrir 'tala' sinnum
                        for i in range(tala): #Keyrir 'tala' sinnum
                              if x==0: #Fyrsta línan
                                    print("A",end="") #Skrifar A 
                              elif x==(tala-1): #Síðasta línan
                                    print("A",end="") #Skrifar A 
                              elif x>0 and i==0: #Fyrsti stafur í línu
                                    print("A",end="") 
                              elif x>0 and i==(tala-1):#Síðasti stafur
                                    print("A",end="") 
                              elif x>0 and i>0: #Allt annað en hitt eiginlega
                                    print("B",end="") 
                        print() # Skiptir um línu
      elif val=="2":
            pass
            
      elif val=="3":
          tala=0
          while tala != 1:
              tala=int(input("Sláðu inn heiltölu "))
              if tala > 1:
                  for i in range(2,tala):
                      if (tala % i) == 0:
                          print(tala,"er ekki prímtala")
                          break
                  else:
                      print(tala,"er prímtala")
          else:
              print(tala,"er ekki prímtala")
          print("Einn er einstök tala")
      elif val=="4":
            nafnalisti=["einar","konni"]
            nafn=random.choice(nafnalisti)
            tempnafn=""
            stafa_geymsla=[]
            for stafur in nafn:
                  tempnafn=tempnafn+"_"
            print("Nafnið sem þú átt að giska a er",tempnafn)
            while tempnafn!=nafn: #Á meðan nafnið er skrifað vitlaust
                  temp=""
                  guess=input("Giskaðu á staf ")
                  for x in range(len(nafn)): #Keyrir jafn oft og hve langt nafnið er
                        if nafn[x]==guess: #Tékkar á öllum stöfunum í nafn
                              temp=temp+nafn[x]
                        elif guess in stafa_geymsla: #Gá hvort það er búið að skrifa staf
                            print("þú ert búinn að nota þennan staf áður!")
                        else:
                            stafa_geymsla.append(guess)
                            if tempnafn[x]!="_": #Búið að giska rétt áður
                                temp=temp+nafn[x]
                            else: #ef það er stjarna verður aftur sett strik
                                temp=temp+"_"
                  tempnafn=temp
                  print("Nafnið sem þú ert að giska á er",tempnafn)
      elif val=="5":
            tala=input("Sláðu inn tölu sem er meira en tveir tölustafir að lengd ")
            fyrsta=tala[0] #Fyrsti tölustafurinn
            snutala=tala[::-1] #Sný tölunni við
            svar=snutala+fyrsta #Set tölurnar saman til að fá svar
            print(svar)#prentar svar
      elif val=="6":
            print("Ókei bæ")
      else:
            print("Rangur Innsláttur")
