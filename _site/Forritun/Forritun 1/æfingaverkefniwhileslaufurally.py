#Höfundur Einar Karl
#Dagsetning 01/10/2018
val=""
#Valmynd
while (val !="10"):
      print("---------------------------------------------------------------")
      print("1. Liður 1")
      print("2. Liður 2")
      print("3. Liður 3")
      print("4. Liður 4")
      print("5. Liður 5")
      print("6. Liður 6")
      print("7. Liður 7")
      print("8. Liður 8")
      print("9. Liður 9")
      print("10. Hætta")
      val=input("Veldu 1, 2, 3, 4, 5, 6, 7, 8, 9 eða 10 til að hætta ")
      if val=="1":
            slett=18
            while slett != 40:
                  slett=slett+2
                  if slett != 40:
                        print(slett,end=", ")
                  else:
                        print(slett)
      elif val=="2":
            tala=15
            sumodd=0
            print("Oddatölurnar milli 15 og 345 eru")
            while tala != 345:
                  if tala%2==1: #Ef tveir gengur ekki upp í töluna þá er hún oddatala
                        sumodd=sumodd +tala
                        print(tala,end=" ")
                  tala=tala+1
            print("\nSumma oddatalnanna er=",sumodd)
      elif val=="3":
            tala=int(input("Sláðu inn tölu undir 100 "))
            while tala != 100:
                  tala=tala+1
                  if tala != 100:
                        print(tala,end=", ")
                  else:
                        print(tala)
      elif val=="4":
            tala=int(input("Sláðu inn tölu stærri en 100 "))
            while tala !=100:
                  tala=tala-1
                  if tala != 100:
                        print(tala,end=", ")
                  else:
                        print(tala)
      elif val=="5":
            tala=int(input("Sláðu inn tölu "))
            if tala%9==0 and tala%5==0 :
                  sinnum9=tala//9
                  sinnum5=tala//5
                  print("9 gengur upp í töluna",sinnum9,"sinnum")
                  print("5 gengur upp í töluna",sinnum5,"sinnum")
            else:
                  print("Talan níu og  fimm ganga ekki báðar upp í",tala)
      elif val=="6":
            tala1=float(input("Sláðu inn kommutölu "))
            tala2=float(input("Sláðu inn aðra kommutölu"))
            deiling=tala1/tala2
            print(tala1,"/",tala2,"=",round(deiling,5))
      elif val=="7":
            #for x in range(1, 1000, 15 and 18) :
                  #print(x)
            teljari=1
            while teljari != 1000:
                  if teljari%15==0 and teljari%18==0: 
                        print(teljari,end="  ")
                  teljari=teljari+1
      elif val=="8":
            teljari=0
            texti="barbara"
            while teljari != 5:
                  print(texti,end="  ")
            texti=texti+"barbara"
      elif val=="9":
            pass
      elif val=="10":
            print("Ókei bæ")
      else:
            print("Rangur Innsláttur")
