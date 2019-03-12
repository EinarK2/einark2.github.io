#Höfundur Einar Karl
#Dags. 5.09.2018
#Liður 1
print("Hello there!")
heiltala1=int(input("Sláðu inn tölu "))
heiltala2=int(input("Sláðu inn aðra tölu "))
if heiltala1 > heiltala2:
      print("Talan sem er minni er",heiltala2)
elif heiltala2 > heiltala1:
      print("Minni talan er",heiltala1)
else:
      print("Tölurnar eru jafnstórar")
#Liður 2
man=input("Sláðu inn nafn mánaðar ")

if man=="januar" or man== "Janúar" or man== "janúar":
      print("Þú slóst inn Janúar")
elif man=="februar" or man=="febrúar" or man=="Febrúar":
      print("Þú slóst inn Febrúar")
elif man=="mars" or man=="Mars":
      print("Þú slóst inn Mars")
elif man=="april" or man=="apríl" or man=="Apríl":
      print("Þú slóst inn Apríl")
elif man=="mai" or man=="maí" or man=="Maí":
      print("Þú slóst inn Maí")
elif man=="juni" or man=="júní" or man=="Júní":
      print("Þú slóst inn Júní")
elif man=="juli" or man=="júlí" or man=="júlí":
      print("Þú slóst inn Júlí")
elif man=="agust" or man=="ágúst" or man=="Ágúst":
      print("Þú slóst inn Ágúst")
elif man=="september" or man=="September":
      print("Þú slóst inn September")
elif man=="oktober" or man=="october" or man=="október" or man=="Október":
      print("Þú slóst inn Október")
elif man=="november" or man=="nóvember" or man=="Nóvember":
      print("Þú slóst inn Nóvember")
elif man=="desember" or man=="december" or man=="Desember":
      print("Þú slóst inn Desember")
else:
      print("Ég þekki ekki þennan mánuð")
#Liður 3
age=int(input("Sláðu inn aldur þinn "))

if age >= 0 and age <= 6 :
      print("Nú, svo þú ferð að byrja í skóla")
elif age >= 7 and age <= 15 :
      skoli=input("Nú, ætlaru í framhaldskóla? ")
      if skoli=="ja" or skoli=="já" or skoli=="Já":
            print("Næs")
      elif skoli=="nei" or skoli=="Nei":
            print("Jæja ok þá...")
      else:
            print("Ok mér var alveg sama hvort eð er")
elif age >= 16 and age <= 105 :
      print("Gangi þér vel í framtíðinni")
else:
      print("Þú hefur svarað spurningunni vitlaust.")
#Liður 4
tala=int(input("Sláðu inn tölu á bilinu 0 til 25 "))
if tala >0 and tala <=25 :
      print("Niðurstaðan er",tala*1.7,"lmao")
else:
            print("Rangur innsláttur")
#Liður 5
svar=input("Hei viltu heyra brandara? ")
if svar=="ja" or svar=="já" or svar=="Já" or svar=="JÁ":
      print("INSERT BRANDARI")
elif svar=="ne" or svar=="nei" or svar=="Nei" or svar=="NEI":
      print("Allt i lagi, kannski seinna")
else:
      print("what")
      
      








