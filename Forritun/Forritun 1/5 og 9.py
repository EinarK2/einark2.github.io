print("Sýnidæmi sem finnur þær tölur sem 5 og 9 ganga upp í \n")
for i in range(1,100000):
      if i % 5==0 and i%9==0:
            print(i,end=" ")
