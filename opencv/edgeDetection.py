import cv2
import numpy as np

img = cv2.imread('assets/garden.png', 0)

img = cv2.goodFeaturesToTrack(img, 100, 0.01, 50)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
