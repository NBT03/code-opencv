import cv2
img1 = cv2.imread(r'C:\Users\ADM\Documents\Zalo Received Files\de_test_pencv\de_test_pencv\anh1.png')
img_hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
cv2.imshow('image' , img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()