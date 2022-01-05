import turtle
import cv2
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

#Gabarito
img = cv2.imread('imgs/iron_man.jpg')

x0 = int(img.shape[0]/2)
y0 = int(img.shape[1]/2)

LENGTH = 260

list_axisXIMG = np.array([])
list_axisYIMG = np.array([])

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

    list_axisXIMG = np.append(list_axisXIMG, x0+int(X*LENGTH))
    list_axisYIMG = np.append(list_axisYIMG, y0+int(-Y*LENGTH))

    img = cv2.circle(img, (x0+int(X*LENGTH), y0+int(-Y*LENGTH)), radius=3, color=(0, 0, 255), thickness=-1)

#Algorithm
def set_goto_pen(dot_i, dot_n, based=0):
    dot_i = dot_i - based
    dot_n = dot_n - based

    t.penup()
    t.goto(list_axisX[dot_i], list_axisY[dot_i])
    
    t.pendown()
    t.goto(list_axisX[dot_n], list_axisY[dot_n])

## Begin-OpenCV & Draw on Turtle Window 
#CONTA OS PIXELS
cimg = img.copy()

before_cnt = np.sum(cimg == 0)
cv2.line(cimg, (int(list_axisXIMG[30]), int(list_axisYIMG[30])), (int(list_axisXIMG[143]), int(list_axisYIMG[143])), (255, 255, 255), thickness=2)
after_cnt = np.sum(cimg == 0)

in_that_line = before_cnt - after_cnt

print(in_that_line)
#FIM DA CONTAGEM


'''
print(len(list_axisY))
set_goto_pen(0, 17)
set_goto_pen(17, 30)
set_goto_pen(30, 143)
'''

TK.mainloop()

#cv2.imshow('img',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()