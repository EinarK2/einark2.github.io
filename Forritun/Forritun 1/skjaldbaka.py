#Höfundur: Einar Karl Pétursson
#Dagsetning 10/17/2018
import turtle
fred=turtle
val=""
while val != "6":
      print("1. Liður 1")
      print("2. Liður 2")
      print("3. Liður 3")
      print("4. Liður 4")
      print("5. Liður 5")
      val=input("Veldu 1-5 eða 6 til að hætta ")
      if val=="1":
            fred.reset()
            fred.shape("turtle")
            fred.color("red")
            for i in range (20):
                  fred.width(5)
                  fred.forward(100)
                  fred.up()
                  fred.backward(100)
                  fred.right(90)
                  fred.forward(10)
                  fred.left(90)
                  fred.down()
      elif val=="2":
            fred.reset()
            fred.shape("turtle")
            fred.color("red")
            lina=10
            for i in range (10):
                  fred.width(5)
                  fred.forward(lina)
                  fred.up()
                  fred.backward(lina)
                  fred.right(90)
                  fred.forward(10)
                  fred.left(90)
                  fred.down()
                  lina=lina+20
      elif val=="3":
            fred.reset()
            fred.shape("turtle")
            fred.color("blue")
            radius=10
            for i in range (10):
                  fred.circle(radius)
                  radius=radius+10
      elif val=="4":
            fred.reset()
            fred.shape("turtle")
            fred.color("blue")
            radius=10
            for i in range (15):
                  fred.circle(radius)
                  fred.up()
                  fred.right(90)
                  fred.forward(10)
                  fred.left(90)
                  fred.down()
                  radius=radius+10
      elif val=="5":
            import random
            fred.reset()
            fred.shape("turtle")
            fred.color("blue")
            radius=10
            for i in range (10):
                  fred.circle(radius)
                  radius=radius+10
                  horn=random.randint(60,360) #Þetta munstur er eins og munstrið í dæmi 5 nema að það er random í hvaða átt og hve langt það fer
                  lengd=random.randint(20,100)
                  fred.forward(lengd)
                  fred.left(horn) 
      elif val=="6":
            print("Ókei BÆ")
      else:
            print("Rangur Innsláttur")
            
