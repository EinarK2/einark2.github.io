f = open("æfing2.txt","w",encoding = 'utf-8')
for x in range(5):
    tala = int(input("Sláðu inn tölu "))
    f.write(str(tala)+" ")
f.close()