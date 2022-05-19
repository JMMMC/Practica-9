import cv2
import numpy as np

def T_M(img,tem):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    tem_gray = cv2.cvtColor(tem, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(img_gray, tem_gray, cv2.TM_CCOEFF_NORMED)
    threshold = 0.85
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + tem.shape[1], pt[1] + tem.shape[0]), (0,255,255), 2)

    return img

def Impresion(namme,imagen,x,y):
    cv2.namedWindow(namme)
    cv2.moveWindow(namme, x,y)
    cv2.imshow(namme, imagen)

img = cv2.imread('Meine_Familie.jpg')
chema = cv2.imread('Chema.jpg')
yuxal = cv2.imread('Yuxal.jpg')
ab = cv2.imread('Abraham.jpg')

img = T_M(img,chema)
img = T_M(img,yuxal)
img = T_M(img,ab)

Impresion('Meine Familie',img,50,50)
Impresion('Chema',chema,700,200)
Impresion('Yuxal',yuxal,900,200)
Impresion('Abraham',ab,1100,200)

cv2.waitKey(0)
cv2.destroyAllWindows()
