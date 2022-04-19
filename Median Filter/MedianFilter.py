import cv2
import numpy

img = cv2.imread("fiony.jpg")
dst = cv2.medianBlur(img, 7)

cv2.imshow('image', numpy.hstack((img, dst)))
cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.waitKey(1)