#ÇARPIM TABLOSU TEST UYGULAMASI

import random
print("10 soruluk çarpım tablosu testi")
skor=0
for a in range (10):
    x=random.randint(1,10)
    y=random.randint(1,10)
    soru="{}*{}=".format(x,y)

    d_Cvp=x*y
    cvp=input(soru)
    if int(cvp)==d_Cvp:
        skor+=1
print(f"Doğru sayınız: {skor}")
if skor>8:
    print("Pekiyi")
elif skor>6:
    print("İyi")
elif skor>4:
    print("Orta")
else:
    print("Çok çalışmalısın")
