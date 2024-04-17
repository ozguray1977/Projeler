#Çizilmek istenen köşe sayısı kadar çokgen çizimi

from turtle import *

n=int(input("Köşe sayısını girin: "))
aci=360/n   #çizilen çokgenin açılarını hesaplar
pensize(10)

for i in range(n):
    forward(50)
    left(aci)
print(f"Açı değerleri {aci} derecedir")
done()
