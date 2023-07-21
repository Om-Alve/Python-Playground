import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    height = int(cam.get(4))
    width = int(cam.get(3))
    frame = cv2.flip(frame, 1)
    # frame = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    # frame = cv2.line(frame, (width, 0), (0, height), (255, 0, 0), 10)
    # frame = cv2.rectangle(frame, (100, 100), (200, 200), (100, 100, 100), 5)
    # frame = cv2.circle(frame, (width//2, height//2), 200, (0, 0, 255), 5)
    frame = cv2.putText(frame, 'Om Alve', (10, height-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
