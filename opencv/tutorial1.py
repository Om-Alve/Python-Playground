import cv2
import random
img = cv2.imread("assets/Garden.png", -1)

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('image', img)

cv2.imwrite('Grayscale.png', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
