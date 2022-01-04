import turtle
import math as m
import numpy as np

s = turtle.getscreen()  
turtle.title("Testandoooo")
t = turtle.Turtle()

#SETUP
LENGTH = 200
list_axisX = np.array([])
list_axisY = np.array([])

t.penup()
t.goto(0,-LENGTH)

t.pendown()
t.circle(LENGTH)

t.penup()
t.goto(LENGTH, 0)

qtd_p = 36

for i in range(0, 360, int(360/qtd_p)):
    X = m.cos((m.pi/180)*i)
    Y = m.sin((m.pi/180)*i)

    list_axisX = np.append(list_axisX, X)
    list_axisY = np.append(list_axisY, Y)

    t.goto(X*LENGTH, Y*LENGTH)
    t.pendown()
    t.dot(10)
    t.penup()

#Algorithm
