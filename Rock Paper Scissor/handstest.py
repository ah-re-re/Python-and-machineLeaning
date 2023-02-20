import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
detector = HandDetector(maxHands=1)

while True:
    imgBG = cv2.imread("Resources/BG.png")

    success, img = cap.read()

    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480]

    hands, img = detector.findHands(img)  # with draw

    if hands:
        hands = hands[0]
        filter = detector.fingersUp(hands)
        print(filter)



    cv2.imshow("BD", imgBG)
    cv2.imshow("Image", img)
    cv2.imshow("Scaled", imgScaled)


    cv2.waitKey(1)
