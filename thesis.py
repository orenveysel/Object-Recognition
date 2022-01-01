import cv2
import numpy as np


camera = cv2.VideoCapture(0)
while True:
    x,y = camera.read()
    cv2.imshow("Object Recognition", y)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
