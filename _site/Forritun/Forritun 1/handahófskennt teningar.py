import random
ten1=0
ten2=0
ten3=0
teljari=1
svar=" "
while teljari <= 3 and svar!="n":
      ten1=random.randint(1,6)
      ten2=random.randint(1,6)
      ten3=random.randint(1,6)
      teljari=teljari+1
      print(ten1,ten2,ten3)
      svar=input("Kasta aftur (j/n)?")
