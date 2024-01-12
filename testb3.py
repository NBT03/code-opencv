import cv2
import numpy as np

frame = cv2.imread(r'C:\Users\ADM\Documents\Zalo Received Files\de_test_pencv\de_test_pencv\anh3.png',1)
img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(img,30,255,cv2.THRESH_BINARY)
countrours,_= cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

font = cv2.FONT_HERSHEY_SIMPLEX

for cnt in countrours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True), True)
    cv2.drawContours(frame, [approx], -1, (0,255,0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 0:
        cv2.putText(frame,"hinhtron",(x,y),font,2,cv2.LINE_AA)

cv2.imshow('ouput ',frame)
cv2.imshow('threshold',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
