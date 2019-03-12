nafn="Einar Karl"
print(nafn[7])
for stafur in nafn:
      print(stafur)
print(len(nafn))
for x in range(len(nafn)):
      print(nafn[x],end="*")
print(nafn[0:6])
print(nafn[6:10])
print(nafn.upper())
print(nafn.lower())
stafur="n"
nafn=nafn.replace(stafur,"#")
print(nafn)
texti="konni er hér að forrita eða skrifa textann"
telja=0
for stafur in texti:
      if stafur=="n":
            telja=telja+1
print("Fjöldi enn í textanum er",telja)
