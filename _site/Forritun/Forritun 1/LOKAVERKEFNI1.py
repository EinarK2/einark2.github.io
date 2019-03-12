#Höfundur Einar Karl Pétursson
val=" "
while val!="7": #Valmynd
      print("1. Skipting í fótboltalið")
      print("2. Summa")
      print("3. Fjórir dálkar, tuttugu raðir")
      print("4. Skipta um tákn í texta")
      print("5. BMI stuðull.")
      print("6. 7 tölur í fylki")
      print("7. Hætta")
      val=input("Veldu 1-6 eða 7 til að hætta ")
      if val=="1":
            fjoldi=int(input("Fjöldi þáttakenda ? ")) #Tekur inn fjölda þáttakenda
            fjoldilid=int(input("Fjöldi í hverju liði? ")) #Tekur inn fjölda liða
            lidafjoldi=fjoldi//fjoldilid #Fjöldi liða
            varamenn=fjoldi % fjoldilid #Fjöldi varamanna
            print("Niðurstöður")
            print("Liðafjöldi",lidafjoldi)
            print("Varamenn",varamenn)
      elif val=="2":
            tala=1
            svar=1
            while svar!=0: #Þetta forrit tekur heiltölu og reiknar summu talna í 0
                  tala=int(input("Sláðu inn tölu "))
                  svar=tala
                  if tala < 0: #Mínus tölur 
                        summa=0
                        while tala !=-1:
                              summa=summa+tala
                              print("(",tala,") +",end=" ")
                              tala=tala+1
                        if tala != 0:
                              print("(",tala,")",end=" ")
                        print("=",summa)
                  elif tala > 0: #Plús tölur
                        summa=0
                        while tala !=1:
                              summa=summa+tala
                              print(tala,"+",end=" ")
                              tala=tala-1
                        if tala != 0: #Þetta er svo útreikningurinn endar ekki á - eða + eða 0
                              print(end=" ")
                        print(tala,"=",summa) #Svar
                  elif tala==0: #Þegar notandinn skrifar 0 þá hættir forritið
                        print("Takk fyrir að nota forritið mitt")
      elif val=="3":
             d1=1 #Skilgreini dálka
             d2=1
             d3=1
             d4=0
             summa=0 #Skilgreini líka summu
             for x in range(25): #Keyrir 25 sinnum
                   d3=d1*d2
                   summa=d1+d2+d3+d4
                   d4=summa
                   print(d1," ",d2," ",d3," ",d4) #Sýnir þetta í hvert sinn ssem það keyrir
                   d1=d1+1
                   d2=d2+2
      elif val=="4":
            texti=input("Sláðu inn texta ")
            for x in texti:
                  if x != "S" and x != "s" and x != "A" and x != "a" and x != "N" and x != "n":
                        texti.replace(x,"*")
            print(texti)
      elif val=="5":
            flag=True #skilgreini flag 
            nafn=input("Hvað heitir notandinn? ") #Spyr hvað notandinn heitir
            while flag==True: #Eftirfarandi er til að vera viss um að notandi skrifar kk eða kvk rétt (Líka spurt um kíló eftir kyni)
                  kyn=input("Hvaða kyn ertu (KK/KVK)? ")
                  if kyn=="KK" or kyn=="kk":
                        kilo=int(input("Hvað ertu þungur í kílóum? "))
                        flag=False
                  elif kyn=="KVK" or kyn=="kvk":
                        kilo=int(input("Hvað ertu þung í kílóum? "))
                        flag=False
                  else:
                        print("Þú skrifaðir kyn vitlaust")
                        flag==True #set flag sem True svo forritið keyrir aftur
            haed=float(input("Hver er hæð þín í metrum? ")) #Spyr um hæð (ekki kynjaskipt)
            BMI=float(kilo/(haed*haed)) #Reiknar BMI Stuðul
            print("BMI Stuðull þinn er",round(BMI,2)) #Sýnir BMI stuðullinn
            #Hér kemur texti ef viðkomandi er karlkyns:
            if BMI < 18.5 and kyn=="KK" or BMI < 18.5 and kyn=="kk":
                  print("Þú ert of grannur miðað við hæð",nafn)
            elif BMI >=18.5 and BMI <=24.9:
                  print("Þú ert með fína þyngd miðað við hæð",nafn)
            elif BMI >=25.0 and BMI <=29.9 and kyn=="KK" or BMI >=25.0 and BMI <=29.9 and kyn=="kk":
                  print("Þú ert of þungur miðað við hæð",nafn)
            elif BMI > 30 and kyn=="KK" or BMI > 30 and kyn=="kk":
                  print("Þú ert óeðliga þungur miðað við hæð",nafn)
            #Hér kemur texti ef viðkomandi er kvenkyns:
            elif BMI < 18.5 and kyn=="KVK" or BMI < 18.5 and kyn=="kvk":
                  print("Þú ert of grönn miðað við hæð",nafn)
            elif BMI >=25.0 and BMI <=29.9 and kyn=="KVK" or BMI >=25.0 and BMI <=29.9 and kyn=="kvk":
                  print("Þú ert of þung miðað við hæð",nafn)
            elif BMI > 30 and kyn=="KVK" or BMI > 30 and kyn=="kvk":
                  print("Þú ert óeðliga þung miðað við hæð",nafn)
            else: #Bara til öryggis ef það er einhver villa
                  print("Villa")
      elif val=="6":
            listi=[] #Skilgreinir lista
            teljari=0 #Skilgreinir teljara
            while teljari < 7: #Keyrir sjö sinnum
                  tala=int(input("Sláðu inn tölu númer "+str(teljari+1)+" ")) #Biður um tölu
                  listi.append(tala) #Setur tölu í lista
                  teljari=teljari+1 
            print("Hæðsta talan er",max(listi)) #Sýnir hæðstu tölu
            print("Lægsta talan er",min(listi)) #Sýnir minnstu tölu
            print("Summa talnanna er",sum(listi)) #Sýnir summu
            medaltal=sum(listi)/len(listi) #Reiknar meðaltal
            print("Meðaltal talna er",round(medaltal,2)) #Sýnir meðaltal
      elif val=="7":
            print("Ókei bæ")
      else: #Ef skrifað er annað en það sem er beðið um
            print("Rangur Innsláttur")
