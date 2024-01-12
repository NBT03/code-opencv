import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread(r'C:\Users\ADM\Documents\Zalo Received Files\de_test_pencv\de_test_pencv\anh2.PNG', 0)
kernel = np.ones((35, 35), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img3 = opening
kernel3 = np.ones((35, 35), np.uint8)
closing = cv2.morphologyEx(img3, cv2.MORPH_CLOSE, kernel3)
titles = ['input ','output 1','output 2']
image = [img, opening, closing]
for i in range(3):
    plt.subplot(2,3,i+1),plt.imshow(image[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
