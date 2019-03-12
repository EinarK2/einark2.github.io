f = open("æfing2.txt",'r',encoding = 'utf-8')
innihald = f.read()
f.close()
print(innihald)

listi=list(innihald)
x=' '
for x in listi:
    listi.remove(' ')
listi = list(map(int, listi))
medaltal=sum(listi)/len(listi)
print(round(medaltal,2))