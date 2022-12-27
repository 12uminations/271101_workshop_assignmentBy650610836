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
            if f1[0]==0:
                if "Thumb1" in Fing:
                    Fing.remove("Thumb1")
            if f1[0]==1:
                if "Thumb1" not in Fing:
                    Fing.insert(0,"Thumb1")
            if f1[1]==0:
                if "Index Finger1" in Fing:
                    Fing.remove("Index Finger1")
            if f1[1]==1:
                if "Index Finger1" not in Fing:
                    Fing.insert(1,"Index Finger1")
            if f1[2]==0:
                if "Middle Finger1" in Fing:
                    Fing.remove("Middle Finger1")
            if f1[2]==1:
                if "Middle Finger1" not in Fing:
                    Fing.insert(2,"Middle Finger1")
            if f1[3]==0:
                if "Ring Finger1" in Fing:
                    Fing.remove("Ring Finger1")
            if f1[3]==1:
                if "Ring Finger1" not in Fing:
                    Fing.insert(3,"Ring Finger1")
            if f1[4]==0:
                if "Pinky1" in Fing:
                    Fing.remove("Pinky1")
            if f1[4]==1:
                if "Pinky1" not in Fing:
                    Fing.insert(4,"Pinky1")
    if len(hands)==2:
            hands2=hands[1]
            f2=detector.fingersUp(hands2)
            if f2[0]==0:
                if "Thumb2" in Fing2:
                    Fing2.remove("Thumb2")
            if f2[0]==1:
                if "Thumb2" not in Fing2:
                    Fing2.insert(0,"Thumb2")
            if f2[1]==0:
                if "Index Finger2" in Fing2:
                    Fing2.remove("Index Finger2")
            if f2[1]==1:
                if "Index Finger2" not in Fing2:
                    Fing2.insert(1,"Index Finger2")
            if f2[2]==0:
                if "Middle Finger2" in Fing2:
                    Fing2.remove("Middle Finger2")
            if f2[2]==1:
                if "Middle Finger2" not in Fing2:
                    Fing2.insert(2,"Middle Finger2")
            if f2[3]==0:
                if "Ring Finger2" in Fing2:
                    Fing2.remove("Ring Finger2")
            if f2[3]==1:
                if "Ring Finger2" not in Fing2:
                    Fing2.insert(3,"Ring Finger2")
            if f2[4]==0:
                if "Pinky2" in Fing2:
                    Fing2.remove("Pinky2")
            if f2[4]==1:
                if "Pinky2" not in Fing2:
                    Fing2.insert(4,"Pinky2")


    Nfing=len(Fing)+len(Fing2)
    cv2.putText(img, str(Fing), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1.1,
                (255, 0, 255), 2)
    cv2.putText(img, str(Fing2), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1.1,
                (255, 0, 255), 2)
    cv2.putText(img, str(Nfing), (10, 170), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    
                
    img = cv2.imshow("Image", img)
    
    if cv2.waitKey(1)&0xFF==27:
        break
cap.relase()
#Closeing all open windows
cv2.destroyAllWindows()