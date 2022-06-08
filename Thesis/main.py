# Call all the libraries that we use

from turtle import width
import cv2
from matplotlib.pyplot import contour
from tracker import *

# Create tracker object

tracker = EuclideanDistTracker()

cap = cv2.VideoCapture("highway.mp4")

history=100
varThreshold=35

# Object detection from a Stable camera

object_detector = cv2.createBackgroundSubtractorMOG2(history, varThreshold)

while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape

    # Extract Region of interest

    leftdown = 220
    rightdown = 350
    leftup = 380
    rightup = 600

    closer = frame[leftdown:rightdown,leftup:rightup]

    # Object Detection

    mask = object_detector.apply(closer)
    coor = 255
    _, mask = cv2.threshold(mask, coor-1, coor, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []

    for cnt in contours:

        # Calculate area and remove small elements

        area = cv2.contourArea(cnt)
        if area > 100:

            x, y, w, h = cv2.boundingRect(cnt)
            detections.append([x, y, w, h])

    # Object Tracking 

    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(closer, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        cv2.rectangle(closer, (x, y), (x + w, y +h), (0, 255, 0), 3)

    # Open screens and give title for screens

    cv2.imshow("Closer", closer)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    # Assing "q" key for quitting the program

    key = cv2.waitKey(30)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
