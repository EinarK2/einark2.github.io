#Höfundur Einar Karl Pétursson 27/08/2018
#Liður 1
print("#Liður 1")
nafn=input("Hvað heitir notandinn? ") #Forritið spyr notandann um nafn
#Útskrift
print("Velkominn í áfangann FOR1TÖ3AU",nafn+".","Þetta verður skemmtileg önn, ég hlakka til að læra forritun.")
#Liður 2
print("#Liður 2")
tala=float(input("Sláðu inn kommutölu með þrem aukastöfum. ")) #Forritið spyr notandann um einhverja tölu með þrem aukastöfum
#Útskrift
print("Þú hefur valið töluna:",round(tala,1))
#Liður 3
print("#Liður 3")
tala2=int(input("Sláðu inn tölu ")) #Forritið spyr notandann um tvær tölur
tala3=int(input("Sláðu inn aðra tölu "))
#Útskrift
print("Margfeldi talnanna er:",tala2*tala3)
print("Frádráttur talnanna er:",tala2-tala3)
#Liður 4
print("#Liður 4")
haed=int(input("Sláðu inn hæð á kassa ")) #Forritið spyr notandann um hæð, lengd, og breidd á kassa
lengd=int(input("Sláðu inn lengd kassans "))
breidd=int(input("Sláðu inn breidd kassans "))
#Útskrift
print("Rúmmál kassans er:",haed*lengd*breidd)
#Liður 5
print("#Liður 5")
aldur1=int(input("Hver er aldur þinn? ")) #Forritið spyr um aldur notandanns og einnig pabba hans
aldur2=int(input("Hver er aldur pabba þíns? "))
#Útskrift
print("Pabbi þinn var",aldur2-aldur1,"ára þegar þú fæddist")
#Liður 6
print("#Liður 6")
aldur3=int(input("Sláðu inn aldur á einstaklingi ")) #Forritið spyr um aldur á þrem einstaklingum.
aldur4=int(input("Sláðu inn aldur á öðrum einstaklingi "))
aldur5=int(input("Sláðu inn aldur á öðrum einstaklingi "))
medaltala=aldur3+aldur4+aldur5 #Hér er summan á öldrunum
#Útskrift
print("Meðalaldur einstaklingana er",medaltala/3)
#Lok
print("Gaman að geta aðstoðað þig við þessa útreikninga",nafn+".","Hafðu það gott í dag :)")
