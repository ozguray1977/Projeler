from turtle import *
import time

title("CHP BAYRAĞI")    #BAŞLIK
ok = Turtle()
bgcolor("red")  #ARKA PLAN RENGİ
ok.speed(10)    #ÇİZİM HIZI

ok.pensize(10)  # Kalem kalınlığını

ok.color("white")   # Kalem rengini ve iç rengini ayarla

time.sleep(2)

def ok1():
    ok.forward(180)
    ok.right(150)   # Okun uç kısmını çiz
    ok.forward(25)
    ok.backward(25)
    ok.left(300)
    ok.forward(25)
    ok.left(120)
    ok.forward(25)
    ok.backward(25)
    ok.penup() 

def ok2(x,y,angle):
    ok.penup()
    ok.goto(x, y)
    ok.setheading(angle)
    ok.pendown()
    ok.forward(280)
    ok.right(150)
    ok.forward(25)
    ok.backward(25)
    ok.left(300)
    ok.forward(25)
    ok.left(120)
    ok.forward(25)
    ok.backward(25)
    ok.right(150)
    ok.penup()

def ok3(x,y,angle):
    ok.penup()
    ok.goto(x, y)
    ok.setheading(angle)
    ok.pendown()
    ok.forward(330)
    ok.right(150)
    ok.forward(25) 
    ok.backward(25)
    ok.left(300)
    ok.forward(25)
    ok.left(120)
    ok.forward(25)
    ok.backward(25)
    ok.right(150)
    ok.penup()

def ok4(x,y,angle):
    ok.penup()
    ok.goto(x, y)
    ok.setheading(angle)
    ok.pendown()
    ok.forward(280)
    ok.right(150)
    ok.forward(25)
    ok.backward(25)
    ok.left(300)
    ok.forward(25)
    ok.left(120)
    ok.forward(25)
    ok.backward(25)
    ok.right(150)
    ok.penup()

def ok5(x,y,angle):
    ok.penup()
    ok.goto(x, y)
    ok.setheading(angle)
    ok.pendown()
    ok.forward(230)
    ok.right(150)
    ok.forward(25)
    ok.backward(25)
    ok.left(300)
    ok.forward(25)
    ok.left(120)
    ok.forward(25)
    ok.backward(25)
    ok.right(150)
    ok.penup()

def ok6(x,y,angle):
    ok.penup()
    ok.goto(x, y)
    ok.setheading(angle)
    ok.pendown()
    ok.forward(180)
    ok.right(150)
    ok.forward(25)
    ok.backward(25)
    ok.left(300)
    ok.forward(25)
    ok.left(120)
    ok.forward(25)
    ok.backward(25)
    ok.right(150)
    ok.penup()

def yazi(x,y):  #CHP yazısı
    ok.penup()
    ok.goto(x, y)
    ok.pendown()
    ok.write("CHP",font=('Arial Black', 65, 'normal'))

def dikdortgen(x,y): # yazı ve okların etrafı çerçeve
    ok.penup()
    ok.goto(-40,-130)
    ok.pendown()    
    ok.forward(-600)  
    ok.right(90)
    ok.forward(380)  
    ok.right(90)
    ok.forward(-600)  
    ok.left(90)
    ok.forward(-380)  

def ucgen(x,y): #okun çentiği 
    ok.penup()
    ok.pensize(2)
    ok.goto(x,y)
    ok.pendown()
    ok.color("red")
    ok.begin_fill()
    ok.forward(8)  
    ok.backward(8)
    ok.left(300)
    ok.forward(8)
    ok.left(120)
    ok.forward(8)
    ok.backward(8)    
    ok.right(150)
    ok.end_fill()
    ok.penup()

ok1()
ok2(-2,10,12)
ok3(-7,20,24)
ok4(-12,30,36)
ok5(-17,40,48)
ok6(-22,50,60)
yazi(0,-130)
dikdortgen(-50,180)
ucgen(-10,16)
time.sleep
import bayrak
done()