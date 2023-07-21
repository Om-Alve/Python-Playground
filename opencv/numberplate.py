import numpy as np
import cv2

frame = cv2.imread('assets/car1.jpg')
cv2.imshow('a', frame)
numberplate_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_license_plate_rus_16stages.xml')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 75, 200)
number_plate = numberplate_cascade.detectMultiScale(edged, 1.2)
for x, y, h, w in number_plate:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
cv2.imshow('frame', edged)
cv2.waitKey(0)
cv2.destroyAllWindows()
