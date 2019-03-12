text=input("Sláðu inn texta: ")
with open("test.txt",'a',encoding = 'utf-8') as f:
    f.write(text)
print(text,"hefur verið skrifaður í skránna skra.txt")