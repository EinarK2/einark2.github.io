#Höfundur Einar Karl
#Dagsetning 15/10/2018
val=""
#Valmynd
while val != "9":
      print("-------------------------------------------------------------")
      print("1. Liður 1")
      print("2. Liður 2")
      print("3. Liður 3")
      print("4. Liður 4")
      print("5. Liður 5")
      print("6. Liður 6")
      print("7. Liður 7")
      print("8. Liður 8")
      print("9. Hætta")
      val=input("Veldu 1, 2, 3, 4, 5, 6, 7, 8 eða 9 til að hætta ")
      if val=="1":
            for i in range(1,6) :
                  print(i)
      elif val=="2":
            for i in range(2,11,2):
                  print(i)
      elif val=="3":
            for i in range(30,41):
                  print(i)
      elif val=="4":
            for i in range(100,201,4):
                  print(i)
      elif val=="5":
            teljari=1
            for i in range(10,34):
                  print(i,end="  ")
                  if teljari%6==0: #Eftir 6 tölur skiptir um línu
                        print()
                  teljari=teljari+1
      elif val=="6":
            for i in range(1,6):
                  print("A"*i)
      elif val=="7":
            for i in range(1,6):
                  print(str(i)*i)
      elif val=="8":
            for i in range(5,0,-1):
                  print("A"*i)
      elif val=="9":
            print("Ókei bæ")
      else:
            print("Rangur innsláttur")
      
