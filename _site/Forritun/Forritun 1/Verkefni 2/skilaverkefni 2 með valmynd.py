#Höfundur Einar Karl P
#Dagsetning 10.09.2018 og 12.09.2018
val=""
#Valmynd
print("1. Liður 1")
print("2. Liður 2")
print("3. Liður 3")
print("4. Liður 4")
print("5. Liður 5")
print("6. Hætta")
val=input("Veldu 1, 2, 3, 4, 5 eða 6 til að hætta ") #Biður um val
if val=="1": #Ef valið er 1
      #Liður 1
      print("Hæ þarna")
      print("#Liður 1")
      tala1=int(input("Sláðu inn heiltölu "))
      tala2=int(input("Sláðu inn aðra heiltölu ")) #Forrtitið spyr um þrjár heiltölur
      tala3=int(input("Sláðu inn aðra heiltölu "))
      #Útskrift
      if tala1==tala2 or tala2==tala3 or tala3==tala1: #Hér reiknar forritið hvort eitthvað af tölunum eru alveg eins
            print("Þú sláðir inn tölur sem voru alveg eins")
      else:
            if(tala1<tala2) and (tala1<tala3):
                  if tala2<tala3:
                        print("Tala",tala2,"er í miðjunni")
                  else:
                        print("Tala",tala3,"er í miðjunni") #Hér eru allskonar reikningar til að finna út hvaða tala er í miðjunni
            elif(tala2<tala1) and (tala2<tala3):
                  if tala1<tala3:
                        print("Tala",tala1,"er í miðjunni")
                  else:
                        print("Tala",tala3,"er í miðjunni")
            elif (tala3<tala1) and (tala3<tala2):
                  if tala1<tala2:
                        print("Tala",tala1,"er í miðjunni")
                  else:
                        print("Tala",tala2,"er í miðjunni")
elif val=="2": #Ef valið er 2
      #Liður 2
      print("#Liður 2")
      svar=input("Á að breyta tommur í sentimetra eða sentimetra í tommur? ") #Hér spyr forritið hvort á breyta tommum í sentimetra eða öfugt
      #Útskrift
      if svar=="tommur" or svar=="Tommur" or svar=="inch" or svar=="inches": #Hér athugar forritið hvort svarað var tommur 
            tommur=float(input("Sláðu inn tommu lengd "))    #Svo spyr það um lengd tommunnar
            cm=tommur*2.54    #Hér reiknar það hvað það er í sentimetrum
            print(tommur,"tommur er",cm,"í sentimetrum") #Útskrift
      elif svar=="sentimetrar" or svar=="Sentimetrar"or svar=="sentimetra" or svar=="cm": #Hér er sama nema með sentimetrum
            sentimetrar=float(input("Sláðu inn sentimetra lengd "))
            inch=sentimetrar*0.39370079 
            print(sentimetrar,"sentimetrar er",round(inch,2),"í tommum") #Útskrift
      else:
            print("Rangur Innsláttur") #Hér kemur þetta ef notandinn skrifar eitthvað annað en sentimetra eða tommur
elif val=="3": #Ef valið er 3
      #Liður 3
      print("#Liður 3")
      month=int(input("Sláðu inn númer mánaðar ")) #Hér spyr forritið um númer á mánuði 
      #Útskrift
      if month >=1 and month <=3:
            print("Nú er daginn tekið að lengja.")
      elif month >=4 and month <=5:
            print("Vorið er komið og grundirnar gróa.")
      elif month >=6 and month <=8:                               #Hér athugar forritið hvaða mánuð var sleginn inn og segir eitthvað sem er byggt á mánuðnum
            print("Núna er sumarið komið með blóm í haga.")
      elif month >=9 and month <=10:
            print("Núna er haustið gengið í garð.")
      elif month >=11 and month <=12:
            print("Núna styttist í jólin.")
      else:
            print("Rangur innsláttur") #Hér segir forritið þetta ef notandinn skrifar eitthvað vitlaust
elif val=="4": #Ef valið er 4
      #Liður 4
      print("#Liður 4")
      nafn=input("Hvað heitir notandinn? ") # Hér á eftir spyr forritið hvað notandinn heitir og hvaða kyn notandinn er og síðan er spurt um tvær tölur
      kyn=input("Ertu karl eða kona? ")
      nr1=int(input("Sláðu inn tölu "))
      nr2=int(input("Sláðu inn aðra tölur "))
      #Útskrift
      if kyn=="Karl" or kyn=="karl" or kyn=="kk" or kyn=="kall" or kyn=="KARL":
            print("Blessaður",nafn)
      elif kyn=="kona" or kyn=="Kona" or kyn=="kvk" or kyn=="KONA": #Hér kannar forritið hvort var skrifað karl eða kona og segir svo eitthvað byggt á því
            print("Blessuð",nafn)
      else:
            print("Blessaður eða blessuð ég veit ekki hvors kyns þú ert") #Þetta er skrifað ef notandinn skrifaði eitthvað annað en karl eða kona
      #Útskrift 2
      if nr1<nr2: #Hér reiknar forritið hvor talan en er stærri hvort að mismunurinn er stærri eða minni en 100
            print(nr2,"er stærri talan")
            mismunur=nr2-nr1
            if mismunur>100:
                  print("Mismunurinn er stærri en 100")
            else:
                  print("Mismunurinn er minni en 100")
      elif nr2<nr1: #Sama hér
            print(nr1,"er stærri talan")
            mismunur=nr1-nr2
            if mismunur>100:
                  print("Mismunurinn er stærri en 100")
            else:
                  print("Mismunurinn er minni en 100")   
      else:
            print("Tölurnar eru jafnstórar") #Þetta kemur ef notandinn slær inn tvær eins tölur
elif val=="5": #Ef valið er 5
      #Liður 5
      print("#Liður 5")
      number=int(input("Sláðu inn tölu sem er lægri en 0 eða hærri en 10 ")) #Hér spyr forritið um tölu sem er lægri en 0 eða hærri en 10
      #Útskrift
      if number >0 and number <10:
            print("Þessi tala er ekki lægri en núll eða hærri en 10") #Hér reiknar forritið út hvort talan er lægri en 0 eða hærri en 10 
      else:
            print("Vel gert!") #Hér ef að það er það sem var beðið um þá segir forritið "Vel gert"
elif val=="6": #Ef valið er 6
      print("Ókei Bæ")
else:
      print("Rangur innsláttur")





