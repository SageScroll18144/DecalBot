import cv2 
import math as m
import numpy as np

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

    list_axisXIMG = np.append(list_axisXIMG, x0+int(X*LENGTH))
    list_axisYIMG = np.append(list_axisYIMG, y0+int(-Y*LENGTH))

    img = cv2.circle(img, (x0+int(X*LENGTH), y0+int(-Y*LENGTH)), radius=3, color=(0, 0, 255), thickness=-1)


#CONTA OS PIXELS
cimg = img.copy()

before_cnt = np.sum(cimg == 0)
cv2.line(cimg, (int(list_axisXIMG[30]), int(list_axisYIMG[30])), (int(list_axisXIMG[143]), int(list_axisYIMG[143])), (255, 255, 255), thickness=2)
after_cnt = np.sum(cimg == 0)

in_that_line = before_cnt - after_cnt

print(in_that_line)
#FIM DA CONTAGEM


print(len(list_axisYIMG))

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()