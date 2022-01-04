import cv2 
import math as m

img = cv2.imread('imgs/iron_man.jpg')

x0 = int(img.shape[0]/2)
y0 = int(img.shape[1]/2)

LENGTH = 260

qtd_p = 144 #qtd de pontos/pregos. Número arbitrário

for i in range(0, 360, int(360/qtd_p)):
    X = m.cos((m.pi/180)*i)
    Y = m.sin((m.pi/180)*i)
    img = cv2.circle(img, (x0+int(X*LENGTH), y0+int(Y*LENGTH)), radius=5, color=(0, 0, 255), thickness=-1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()