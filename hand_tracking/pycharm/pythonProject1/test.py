import cv2
import mediapipe as mp

cap = cv2.VideoCapture("eye_recording.flv")


while True:
   ret, frame = cap.read()
   roi = frame[269: 795, 537: 1416]


   cv2.imshow("Roi", roi)
   key = cv2.waitKey(30)
   if key == 27:
       break

cv2.destroyWindow()