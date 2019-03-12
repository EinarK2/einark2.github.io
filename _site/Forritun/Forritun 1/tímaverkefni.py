#Höfundur: Einar Karl
#Dagsetning 31. okt
#Valmynd
val=" "
while val != "4":
      print("---------------------------------------")
      print("1. Liður 1")
      print("2. Liður 2")
      print("3. Liður 3")
      print("4. Hætta")
      val=input("Veldu 1-3 eða 4 til að hætta ")
      if val=="1":
            aftur=" "
            while aftur !="n":
                  lengd=int(input("Sláðu inn lengd i sentimetrum "))
                  metrar=lengd // 100
                  cm=lengd % 100
                  print(metrar,"metrar")
                  print(cm,"sentimetrar")
                  aftur=input("Viltu keyra forrit aftur? Sláðu inn j ef já, n ef nei: ")
      elif val=="2":
            aftur=" "
            while aftur !="n":
                  tala=int(input("Sláðu inn tölu: "))
                  veldi=int(input("Sláðu inn veldisvísi: "))
                  svar=0
                  for x in range(veldi):
                        svar=tala*(tala*x)
                  print(tala,"í",veldi,"veldi er",svar)
                  aftur=input("Viltu keyra forrit aftur? Sláðu inn j ef já, n ef nei: ")
      elif val=="3":
            aftur=" "
            while aftur !="n":
                  tala=int(input("Sláðu inn tölu á bilinu 1 - 9: "))
                  if tala >=1 and tala <=9:
                        for x in range(tala):
                              print("*"*(tala-x))
                        for x in range(tala):
                              print("*"*(x+1))
                  else:
                        print("Sláðu inn rétt")
                  aftur=input("Viltu keyra forrit aftur? Sláðu inn j ef já, n ef nei: ")
      elif val=="4":
            print("Ókei Bæ")
      else:
            print("Rangur Innsláttur")
            
