import cv2
import numpy as np
from matplotlib import pyplot as plt

imagemTeste = cv2.imread("img/a.jpg")
cor = ('b', 'g', 'r')

for i, col in enumerate(cor):
    hist = cv2.calcHist([imagemTeste], [i], None, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])
    
cv2.imshow("", imagemTeste)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
