#Höfundur Einar Karl
flag=True
val=" " 
while val !="4":
#Valmynd
      print("--------------------------------------")
      print("1. Kennitala")
      print("2. Búa til nýtt orð")
      print("3. Sneið af streng")
      print("4. Hætta")
      val=input("Veldu 1-3 eða 4 til að hætta ")
      if val=="1":
            flag=True
            while flag==True:
                  kt=input("Sláðu inn kennitölu ")
                  sidustu=kt[-2:]
                  if len(kt)==10: #Kannar hvort talan sé af réttri lengd
                        print("Réttur fjöldi stafa") #Útskrift
                  else:
                        print("Ekki réttur fjöldi stafa") #Útskrift ef ekki rétt
                        flag=False#set flag sem false svo forritið keyrir aftur(og í næstu línum)
                  dagur=kt[0:2]
                  intdagur=int(dagur)
                  if intdagur>0 and intdagur<=31:#Kannar hvort dagsetning er rétt
                        print("Rétt Dagsetning")#Útskrift
                  else:
                        print("Röng Dagsetning")#Útskrift
                        flag=False
                  month=kt[2:4]
                  intmonth=int(month)
                  if intmonth>0 and intmonth<=12:#Kannar hvort mánuður er réttur
                        print("Réttur Mánuður") #Útskrift
                  else:
                        print("Rangur mánuður")#Útskrift
                        flag=False
                  sidasti=kt[-1]
                  if sidasti=="0" or sidasti=="9":#Kannar hvort síðasta talan sé 0 eða 9
                        print("Síðasti stafurinn er réttur")#Útskrift
                  else:
                        print("Síðasti stafurinn er rangur")#Útskrift
                        flag=False
                  if flag==False: #Kóði sem kemur ef eitthvað af hinum kóðunum voru false
                        print("Þetta er ekki rétt kennitala, reyndu aftur") #Útskrift
                        flag=True
                  else:
                        print("Vel gert þú slóst inn rétta kennitölu",kt)#Útskrift ef allt er true
                        flag=False
      elif val=="2":
            flag=True
            while flag==True: 
                  texti=input("Sláðu inn orð sem er a.m.k. 5 stafa langt ") #Biður um orð
                  if len(texti)<=4:
                        print("Þetta voru minna en 5 stafir, gerðu aftur ")#Útskrift ef vitlaust
                        flag=True
                  else:
                        fyrst2=texti[0]+texti[1]
                        fyrst2==texti[0:2]
                        seinast2=texti[-2]+texti[-1]
                        seinast2=texti[-2:]
                        #Útskrift
                        print("Nýji strengurinn er:",fyrst2+seinast2)
                        print("Nýji strengurinn í upphafstöfum:",fyrst2.upper()+seinast2.upper())
                        print("Nýji strengurinn í lágstöfum:",fyrst2.lower()+seinast2.lower())
                        flag=False
                  
      elif val=="3":
            nafn=input("Sláðu inn nafn ")#Biður um nafn
            for x in range(len(nafn)):
                  print(nafn[x:len(nafn)])#Útskrift
      elif val=="4":
            print("Ókei bæ")
      else:
            print("Rangur Innsláttur")
