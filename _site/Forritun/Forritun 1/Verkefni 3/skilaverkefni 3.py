#Höfundur Einar Karl
#Dagsetning 24/09/2018
val=""
#While loop
while (val !="6"):
      #Valmynd
      print("------------------------------------------------") #Lína til að láta forritið líta betur út
      print("1. Liður 1 (Tölu innsláttur) ")
      print("2. Liður 2 (Ferhyrnings Reikningur) ")
      print("3. Liður 3 (Leyniorðs innsláttur) ")
      print("4. Liður 4 (Gengur fimm í tölu?) ")
      print("5. Liður 5 (Fleiri reikningar) ")
      print("6. Hætta")
      val=input("Veldu 1, 2, 3, 4, 5 eða 6 til að hætta ")
      if val=="1":
            aftur="já" #Set 'aftur' sem 'já'
            while (aftur == "já" or aftur == "Já"): #svo lengi sem aftur er já þá keyrir forritið
                  tala=int(input("Sláðu inn heiltölu "))#biður um tölu
                  #Útskrift
                  print("Þú hefur valið töluna:",tala)
                  aftur=input("Viltu slá inn aðra heiltölu? ") #Ef valið er 'já' þá keyrir forritið ef ekki þá hættir það
      elif val=="2":
            svar="já" #'svar' er skilgreint
            while (svar == "já" or svar == "Já"): #Á meðan að svarið er já þá keyrir forritið
                  lengd=int(input("Sláðu inn lengd á ferhyrningi "))
                  breidd=int(input("Sláðu inn breidd á ferhyrningi "))
                  #Útskrift
                  print("Flatarmálið er",lengd*breidd) 
                  svar=input("Viltu endurtaka þetta? ")#Ef valið er já þá keyrir forritið annars  ekki
      elif val=="3":
            leyniord="einar" #Leyniorðið er skráð
            svar=0 
            while svar != leyniord: #Á meðan að leyniorðið er ekki rétt þá keyrir forritið
                  svar=input("Skrifaðu leyniorðið þitt ") 
            #Útskrift ef rétt lykilorð er skrifað
            print("Vel Gert")
      elif val=="4":
            tala=int(input("Sláðu inn heiltölu ")) #Beðið er um tölu
            if tala % 5==0: #Ef 5 gengur upp í töluna:
                  #Útskrift
                  print("Talan",tala,"er í fimm sinnum töflunni")
            else: #Útskrift ef fimm gengur ekki upp í töluna
                  print("Talan",tala,"er ekki í fimm sinnum töflunni")
      elif val=="5":
            val2=""
            tel2=0 #val2 og tel2 er skilgreint
            while (val2 !="3"): #Á meðan að valið er ekki 3 keyrir forritið
                  print("------------------------------------------------")
                  tel2=tel2+1 #Teljari fyrir hve oft forritið keyrir
                  print("1. Biður um 10 tölur. Finnur  summu þeirra og meðaltal.")
                  print("2. Biður um tölu og athugar hvort talan sé jöfntala eða oddatala ")
                  print("3. Hætta í forritinu og skrifa ’Ég er frábær forritari’ á skjáinn 10 sinnum og tilgreina hversu oft forritið var keyrt. ")
                  val2=input("Veldu 1, 2 eða 3 ") #Önnur valmynd
                  if val2=="1":
                        telur=-1
                        summa=0
                        while telur<9: #Eftirfarandi kóði er endurtekinn 10 sinnum 
                              telur=telur+1
                              tala=int(input("Sláðu inn tölu "+str(telur+1)+" ")) #Spurt er um tölu
                              summa=summa+tala
                        print("Summa talnanna er",summa)
                        medaltal=summa/10 #Formúla fyrir meðaltölu talnanna
                        #útskrift
                        print("Meðaltal talnanna er",medaltal)
                  elif val2=="2":
                        tala=int(input("Sláðu inn tölu "))
                        if tala % 2==1: #Formúla til að finna hvort talan er oddatala eða ekki
                              #Útskrift
                              print("Þetta er oddatala")
                        else:
                              #Útskrift 2
                              print("Þetta er jöfntala")
                  elif val2=="3":
                        tel=1#Tel er skilgreint
                        while tel<=10: #Eftirfarandi kóði er keyrður 10 sinnum
                              print("Ég er frábær forritari")
                              tel=tel+1
                        #Útskrift
                        print("Aðallúppan hefur keyrt",tel2,"sinnum") #Forritið skrifar hve oft while lúppan keyrði
                  else: #Þetta kemur ef eitthvað annað en 1, 2, eða 3, er skrifað
                        print("Rangur Innsláttur")
      elif val=="6":
            #Útskrift
            print("Ókei Bæ")
            #Hér hættir forritið að keyra
      else:
            print("Rangur Innsláttur")#Ef valið er eitthvað annað en 1 til 6

# Í fyrri kóðanum sem kemur í word skjalinu keyrir kóðinn upp í 10 og hættir svo. Þá er 'i' 0 og hann bætir við sig 1
#Þegar forritið er keyrt þá fer i frá 1 upp í 10. While kóðinn segir forritinu að stoppa þegar 10 kemur
# Í seinni kóðanum er 'i' 1 og þá bætir hann við sig 2. While loopan segir að forritið á að hætta þegar 10 kemur(Heldur áfram á meðan 10 er ekki)
#Þegar maður keyrir samt forritið þá heldur það áfram að eilífu. Ástæðan fyrir því er að forritið fer aldrei upp í 10. Ef það myndi byrja á 0 þá myndi það hætta. 
