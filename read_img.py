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
node_root = 0
node_crrt = 0

#while np.sum(img == 0) != 0:

while True:
    max_v = -(10**9)
    for i in range(len(list_axisXIMG)):
        cimg = img.copy()

        before_cnt = np.sum(cimg == 0)
        cv2.line(cimg, (int(list_axisXIMG[node_root]), int(list_axisYIMG[node_root])),
        (int(list_axisXIMG[i]), int(list_axisYIMG[i])), (255, 255, 255), thickness=2)
        after_cnt = np.sum(cimg == 0)

        in_that_line = before_cnt - after_cnt
        if in_that_line > max_v:
            max_v = in_that_line
            node_crrt = i

    cv2.line(img, (int(list_axisXIMG[node_root]), int(list_axisYIMG[node_root])),
        (int(list_axisXIMG[node_crrt]), int(list_axisYIMG[node_crrt])), (255, 255, 255), thickness=2)
    #draw in turtle

    node_root = node_crrt
    if max_v == 0:
        break
    print(node_crrt)
    print(max_v)
#FIM DA CONTAGEM

print(len(list_axisYIMG))

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()