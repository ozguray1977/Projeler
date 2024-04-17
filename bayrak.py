from turtle import *

title("TÜRK BAYRAĞI")
setup(width=600,height=400)
bgcolor("red")

def renklendirme(renk,x,y):
    penup()
    goto(x,y)
    pendown()
    color(renk)
    begin_fill()

def yildiz():
    renklendirme("white",-140,40)
    for i in range(5):
        forward(50)
        right(144)
        forward(50)
        right(-72)
    end_fill()

def hilal(cap):
    circle(cap)
    end_fill()

renklendirme("white",-300,-120)
hilal(130)
renklendirme("red",-260,-90)
hilal(100)

yildiz()
mainloop()
exitonclick()