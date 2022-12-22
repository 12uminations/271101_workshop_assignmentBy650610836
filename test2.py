#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

Nfing = 5
Fing=["Thump", "Index Finger", "Middle Finger", "Ring Finger", "Little Finger"]
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
                    cx8 =cx
                if id == 6:
                    id6 = int(id)
                    cy6 = cy
                    cx6 = cx
            
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                    cx12 = cx
                if id == 10:
                    id10 = int(id)
                    cy10 = cy
                    cx10 = cx

                if id == 16:
                    id16 = int(id)
                    cy16 = cy
                    cx16 = cx
                if id == 14:
                    id14 = int(id)
                    cy14 = cy
                    cx14 = cx

                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                    cx20 = cx
                if id == 18:
                    id18 = int(id)
                    cy18 = cy
                    cx18 = cx
                
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                    cy4 = cy
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                    cy3 = cy

                if id == 5:
                    id5 = int(id)
                    cx5 = cx
                    cy5= cy
                if id == 17:
                    id17 = int(id)
                    cx17 = cx
                    cy17 = cy

                if id==0:
                    id0 = int(id)
                    cy0 = cy
                    cx0 = cx
            #normal case *********************************************************
            if cy8 > cy6:
                if "Index Finger" in Fing:
                    Fing.remove("Index Finger")
            elif cy8 < cy6:
                if "Index Finger" not in Fing:
                    Fing.insert(1,"Index Finger")
            elif cy12 > cy10:
                if "Middle Finger" in Fing:
                    Fing.remove("Middle Finger")
            elif cy12 < cy10:
                if "Middle Finger" not in Fing:
                    Fing.insert(2,"Middle Finger")
            elif cy16 > cy14:
                if "Ring Finger" in Fing:
                    Fing.remove("Ring Finger")
            elif cy16 < cy14:
                if "Ring Finger" not in Fing:
                    Fing.insert(3,"Ring Finger")
            elif cy20 > cy18:
                if "Little Finger" in Fing:
                    Fing.remove("Little Finger")
            elif cy20 < cy18:
                if "Little Finger" not in Fing:
                    Fing.insert(4,"Little Finger")
            #Thump x axis *********************************************************
            elif cx17 > cx5: 
                if cx4 > cx3:
                    if "Thump" in Fing:
                        Fing.remove("Thump")
                if cx4 < cx3:
                    if "Thump" not in Fing:
                        Fing.insert(0,"Thump")
            elif cx17 < cx5:
                if cx4 < cx3:
                    if "Thump" in Fing:
                        Fing.remove("Thump")
                if cx4 > cx3:
                    if "Thump" not in Fing:
                        Fing.insert(0,"Thump")
            #If hand point down *********************************************************
            elif cy0 < cy17:
                if cy8 < cy6:
                    if "Index Finger" in Fing:
                        Fing.remove("Index Finger")
                if cy8 > cy6:
                    if "Index Finger" not in Fing:
                        Fing.insert(1,"Index Finger")
                if cy12 < cy10:
                    if "Middle Finger" in Fing:
                        Fing.remove("Middle Finger")
                if cy12 > cy10:
                    if "Middle Finger" not in Fing:
                        Fing.insert(2,"Middle Finger")
                if cy16 < cy14:
                    if "Ring Finger" in Fing:
                        Fing.remove("Ring Finger")
                if cy16 > cy14:
                    if "Ring Finger" not in Fing:
                        Fing.insert(3,"Ring Finger")
                if cy20 < cy18:
                    if "Little Finger" in Fing:
                        Fing.remove("Little Finger")
                if cy20 > cy18:
                    if "Little Finger" not in Fing:
                        Fing.insert(4,"Little Finger")
            #Thump y axis and other fingers x axis *********************************************************
            # if cx0 > cx5:
            #     if cx4 > cx3:
            #         if "Thump" in Fing:
            #             Fing.remove("Thump")
            #     if cx4 < cx3:
            #         if "Thump" not in Fing:
            #             Fing.insert(0,"Thump")
                
            # if cx0 < cx5:
            #     if cy4 < cy3:
            #         if "Thump" in Fing:
            #             Fing.remove("Thump")
            #     if cy4 > cy3:
            #         if "Thump" not in Fing:
            #             Fing.insert(0,"Thump")
                
            #*******************************************************************************
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