#GÜZEL BİR RESİM ÇİZİMİ

from turtle import *

title("GÜZEL BİR RESİM")
colormode(255)
color(0,0,0)
pensize(5)

def ucgen():
    for a in range(3):
      forward(200)
      left(120)

def kare():
   for a in range(4):
      forward(200)
      right(90)

def kapi(x,y):
      penup()
      goto(0,-200)
      pendown()
      forward(75)
      left(90)
      forward(50)
      right(90)
      forward(50)
      right(90)
      forward(50)
      penup()
      goto(100,-200)
      pendown()
      forward(-50)      
      
def pencere1(x,y):
    penup()
    goto(65,-90)
    pendown()    
    forward(-50)  
    right(90)
    forward(50)  
    right(90)
    forward(-50)  
    left(90)
    forward(-50)

def pencere2(x,y):
    penup()
    goto(135,-90)
    pendown()    
    forward(-50)  
    right(90)
    forward(50)  
    right(90)
    forward(-50)  
    left(90)
    forward(-50)

def direk():
    penup()
    goto(225,-200)
    pendown()    
    forward(225)

def dikdortgen(x,y): # yazı ve okların etrafı çerçeve    
    forward(0)  
    right(90)
    forward(100)  
    left(90)
    forward(-70)  
    right(90)
    forward(-100) 

def renklendirme(renk,x,y):
    penup()
    goto(x,y)
    pendown()
    color(renk)
    begin_fill()

def hilal(cap):
    circle(cap)
    end_fill()

def yildiz():
    renklendirme("white",290,-5)
    for i in range(5):
        forward(9)
        right(144)
        forward(9)
        right(-72)
    end_fill()

def bahce(x,y): # yazı ve okların etrafı çerçeve
    penup()
    goto(0,-120)
    pendown()
    color("black")    
    forward(-100)  
    right(90)
    forward(115)  
    right(90)
    forward(-400)  
    left(90)
    forward(-120)  
    left(90)
    forward(-100)

def yol():
    penup()
    goto(-830,-250)
    pendown()    
    forward(1600)
    penup()
    goto(-830,-350)
    pendown()    
    forward(1600)

def serit(start_point=-830, step=60, cycle=26):
    for i in range(cycle):
        start_point += step
        penup()
        goto(start_point, -300)
        pendown()
        forward(40) 

def gecit(start_point=-250, step=12, cycle=7):
    for i in range(cycle):
        start_point -= step
        penup()
        goto(70, start_point)
        pendown()
        forward(40)
        right(90)
        forward(5)
        right(90)
        forward(40)
        right(90)
        forward(5)
        right(90)  

def gunes(cap):
    circle(cap)
    end_fill()

def agac1():
    penup()
    goto(-700, 0)
    pendown()
    pensize(20)
    pencolor("green")
    left(90)
    speed("fastest")
    dal_agac1(60, 7)

def dal_agac1(uzunluk, seviye):
    if seviye == 0:
        return
    forward(uzunluk)
    left(45)
    dal_agac1(uzunluk * 0.6, seviye - 1)
    right(90)
    dal_agac1(uzunluk * 0.6, seviye - 1)
    left(45)
    backward(uzunluk)

def agac2():
    penup()
    goto(-540, 0)
    pendown()
    pensize(20)
    pencolor("green")
    speed("fastest")
    dal_agac2(60, 7)

def dal_agac2(uzunluk, seviye):
    if seviye == 0:
        return
    forward(uzunluk)
    left(45)
    dal_agac2(uzunluk * 0.6, seviye - 1)
    right(90)
    dal_agac2(uzunluk * 0.6, seviye - 1)
    left(45)
    backward(uzunluk)

def agac3():
    penup()
    goto(-380, 0)
    pendown()
    pensize(20)
    pencolor("green")
    speed("fastest")
    dal_agac3(60, 7)

def dal_agac3(uzunluk, seviye):
    if seviye == 0:
        return
    forward(uzunluk)
    left(45)
    dal_agac3(uzunluk * 0.6, seviye - 1)
    right(90)
    dal_agac3(uzunluk * 0.6, seviye - 1)
    left(45)
    backward(uzunluk)

def agac4():
    penup()
    goto(-620, -120)
    pendown()
    pensize(20)
    pencolor("green")
    speed("fastest")
    dal_agac4(60, 7)

def dal_agac4(uzunluk, seviye):
    if seviye == 0:
        return
    forward(uzunluk)
    left(45)
    dal_agac4(uzunluk * 0.6, seviye - 1)
    right(90)
    dal_agac4(uzunluk * 0.6, seviye - 1)
    left(45)
    backward(uzunluk)

def agac5():
    penup()
    goto(-460, -120)
    pendown()
    pensize(20)
    pencolor("green")
    speed("fastest")
    dal_agac5(60, 7)

def dal_agac5(uzunluk, seviye):
    if seviye == 0:
        return
    forward(uzunluk)
    left(45)
    dal_agac5(uzunluk * 0.6, seviye - 1)
    right(90)
    dal_agac5(uzunluk * 0.6, seviye - 1)
    left(45)
    backward(uzunluk)

begin_fill()
fillcolor(165,42,42)
ucgen()
end_fill()

begin_fill()
fillcolor(128,128,128)
kare()
end_fill()

kapi(0,-200)

begin_fill()
fillcolor(165,42,42)
pencere1(0,0)
end_fill()

begin_fill()
fillcolor(165,42,42)
pencere2(0,0)
end_fill()

direk()

begin_fill()
fillcolor("red")
dikdortgen(0,0)
end_fill()

renklendirme("white",270,-25)
hilal(17)
renklendirme("red",274,-22)
hilal(14) 
yildiz() 
bahce(0,0)
bgcolor("turquoise")
yol()
serit()

begin_fill()
fillcolor("white")
gecit()

renklendirme("yellow",-500,250)
gunes(30)

agac1()
agac2()
agac3()
agac4()
agac5()

done()
