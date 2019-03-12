print("Forrit sem reiknar meðaltal af óákveðnum fjölda talna. Stoppar þegar slegið er inn 0")
tala=-1
teljari=0
summa=0
while tala!=0: #haltu áfram á meðan tala er ekki 0
      tala=int(input("Sláðu inn tölu númer "+str(teljari+1)+" ")) #Les inn tölu
      summa=summa+tala
      if tala !=0: #Telur 0 ekki með
            teljari=teljari+1#Bæti við teljarann
#Kominn út úr slaufunni
medaltal=summa/teljari
print("Meðaltal þessara talna er =",round(medaltal,2))

      
      
