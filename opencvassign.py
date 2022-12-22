#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

Nfing = 5
Fing="Thump, Index Finger, Middle Finger, Ring Finger, Little Finger"
num=1
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 7:
                    id7 = int(id)
                    cy7 = cy
            
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                if id == 11:
                    id11 = int(id)
                    cy11 = cy

                if id == 16:
                    id16 = int(id)
                    cy16 = cy
                if id == 15:
                    id15 = int(id)
                    cy15 = cy

                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                if id == 19:
                    id19 = int(id)
                    cy19 = cy
                
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx

                if id == 5:
                    id5 = int(id)
                    cx5 = cx
                if id == 17:
                    id17 = int(id)
                    cx17 = cx

                      
            if cy8 > cy7:
                if "Index Finger" in Fing:
                    Fing.remove("Index Finger")
            if cy8 < cy7:
                if "Index Finger" not in Fing:
                    Fing.insert(1,"Index Finger")
            if cy12 > cy11:
                if "Middle Finger" in Fing:
                    Fing.remove("Middle Finger")
            if cy12 < cy11:
                if "Middle Finger" not in Fing:
                    Fing.insert(2,"Middle Finger")
            if cy16 > cy15:
                if "Ring Finger" in Fing:
                    Fing.remove("Ring Finger")
            if cy16 < cy15:
                if "Ring Finger" not in Fing:
                    Fing.insert(3,"Ring Finger")
            if cy20 > cy19:
                if "Little Finger" in Fing:
                    Fing.remove("Little Finger")
            if cy20 < cy19:
                if "Little Finger" not in Fing:
                    Fing.insert(4,"Little Finger")
            if cx17 > cx5:
                if cx4 > cx3:
                    if "Thump" in Fing:
                        Fing.remove("Thump")
                if cx4 < cx3:
                    if "Thump" not in Fing:
                        Fing.insert(0,"Thump")
            if cx17 < cx5:
                if cx4 < cx3:
                    if "Thump" in Fing:
                        Fing.remove("Thump")
                if cx4 > cx3:
                    if "Thump" not in Fing:
                        Fing.insert(0,"Thump")
            
               
            Nfing=len(Fing)       

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    cv2.putText(img, str(Fing), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1.2,
                (255, 0, 255), 2)

    cv2.putText(img, str(int(Nfing)), (10, 120), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()