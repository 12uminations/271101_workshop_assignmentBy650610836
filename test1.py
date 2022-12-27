#This code demonstrate how to show location of hand landmark
import cv2
from cvzone.HandTrackingModule import HandDetector 
detector = HandDetector(detectionCon=0.5,maxHands=2)
import mediapipe as mp

cap = cv2.VideoCapture(0)
f1=[None]*5
f2=[None]*5
Fing=["Thumb1", "Index Finger1", "Middle Finger1", "Ring Finger1", "Pinky1"]
Fing2=["Thumb2", "Index Finger2", "Middle Finger2", "Ring Finger2", "Pinky2"]

#*********************************************************************

while True:
    success, img = cap.read()
    hands , img=detector.findHands(img)
    if hands:
            hands1=hands[0]
            f1=detector.fingersUp(hands1)
    if len(hands)==2:
            hands2=hands[1]
            f2=detector.fingersUp(hands2)
            print(f1,f2)
           

        
    img = cv2.imshow("Image", img)
    
    if cv2.waitKey(1)&0xFF==27:
        break
cap.relase()
#Closeing all open windows
cv2.destroyAllWindows()