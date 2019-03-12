#Skilaverkefni 4
#Höfundur: Einar Karl Pétursson
import time
val=" "
while val != "9":
      print("--------------------------------------------------")
      print("1. Liður 1")
      print("2. Liður 2")
      print("3. Liður 3")
      print("4. Liður 4")
      print("5. Liður 5")
      print("6. Liður 6")
      print("7. Liður 7")
      print("8. Liður 8")
      print("9. Hætta")
      val=input("Veldu 1-8 eða 9 til að hætta ")
      if val=="1":
            tala=int(input("Sláðu inn heiltölu "))
            oft=int(input("Hversu oft á að skrifa út þessa tölu? "))
            for x in range(oft): #Útskrift
                  print(tala)
      elif val=="2":
            for i in range(2,15,2):
                  print(i,end=" ") #end er svo það kemur bil á milli talna
            print()#Þetta er til að skipta um línu svo það klessir ekki á valmyndina
      elif val=="3":
            tala1=int(input("Sláðu inn tölu "))
            tala2=int(input("Sláðu inn aðra tölu "))
            for i in range(tala1,tala2+1):#Set +1 svo það endar á tölunni sem sett var inn
                  print(i,end=" ")
            print()#Aftur skipt um línu
      elif val=="4":
            tala1=int(input("Sláðu inn upphafstölu "))
            tala2=int(input("Sláðu inn lokatölu "))
            haekkun=int(input("Sláðu inn hækkun "))
            for i in range(tala1,tala2, haekkun): #Útskrift
                  print(i,end=" ") 
            print() #Skiptir um línu
      elif val=="5":
            tel=1
            for x in range(100,200):
                  print(x,end=" ")
                  if tel % 10 ==0: #Ef 10 gengur upp í tel(tíunda hvert skipti)
                        print()#Skiptir um línu
                  tel=tel+1
      elif val=="6":
            margfald=1
            tala=int(input("Sláðu inn heiltölu "))
            for x in range (1,(tala+1)):
                  margfald=margfald*x
                  if x <tala:
                        print(x,end="*")  #Sýnir útreikning
                  else:
                        print(x,"=",margfald)
      elif val=="7":
            tala=int(input("Veldu tölu á milli 1 og 9 "))
            if tala>=1 and tala<=9:#tala á milli 1 og 9
                  for x in range(tala):
                        print("*"*(x+1))
            else:
                  print("Þú verður að velja tölu á milli 1 og 9")
      elif val=="8":
            arid=int(input("Sláðu inn ártal "))
            if arid % 4==0: #ef 4 gengur upp í árið
                  if arid % 100==0 and arid % 400!=0:
                        print("Það er ekki hlaupár")
                  else:
                        print("Það er hlaupár")
            else:
                  print("Það er ekki hlaupár")
      elif val=="9":
            print("Ókei Bæ")
      else:
            print("Rangur Innsláttur")
