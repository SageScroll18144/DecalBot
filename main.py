import turtle
import math as m
import numpy as np
import tkinter as TK

s = turtle.getscreen()  
turtle.title("Testandoooo")
t = turtle.Turtle()

#SETUP

LENGTH = 260 #ajusta de acordo com a imagem
list_axisX = np.array([])
list_axisY = np.array([])

t.penup()
t.goto(0,-LENGTH)

t.pendown()
t.circle(LENGTH)

t.penup()
t.goto(LENGTH, 0)

qtd_p = 144 #qtd de pontos/pregos. Número arbitrário

for i in np.arange(0, 360, 360/qtd_p):
    X = m.cos((m.pi/180)*i)
    Y = m.sin((m.pi/180)*i)

    list_axisX = np.append(list_axisX, X*LENGTH)
    list_axisY = np.append(list_axisY, Y*LENGTH)

    t.goto(X*LENGTH, Y*LENGTH)
    t.pendown()
    t.dot(10)
    t.penup()

#Algorithm
def set_goto_pen(dot_i, dot_n, based=0):
    dot_i = dot_i - based
    dot_n = dot_n - based

    t.penup()
    t.goto(list_axisX[dot_i], list_axisY[dot_i])
    
    t.pendown()
    t.goto(list_axisX[dot_n], list_axisY[dot_n])

## Begin-OpenCV & Draw on Turtle Window 
print(len(list_axisY))
set_goto_pen(0, 17)
set_goto_pen(17, 30)
set_goto_pen(30, 143)

TK.mainloop()