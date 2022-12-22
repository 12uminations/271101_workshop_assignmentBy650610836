#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp



Nfing= 5
Fing=["Thump", "Index Finger", "Middle Finger", "Ring Finger", "Little Finger"]
#id=list
cy0,cy1,cy2,cy3,cy4,cy5,cy6,cy7,cy8,cy9,cy10,cy11,cy12,cy13,cy14,cy15,cy16,cy17,cy18,cy19,cy20 = cy()
cx0,cx1,cx2,cx3,cx4,cx5,cy6,cx7,cx8,cx9,cx10,cx11,cx12,cx13,cx14,cx15,cx16,cx17,cx18,cx19,cx20 = 0
cy=[cy0,cy1,cy2,cy3,cy4,cy5,cy6,cy7,cy8,cy9,cy10,cy11,cy12,cy13,cy14,cy15,cy16,cy17,cy18,cy19,cy20]
cx=[cx0,cx1,cx2,cx3,cx4,cx5,cy6,cx7,cx8,cx9,cx10,cx11,cx12,cx13,cx14,cx15,cx16,cx17,cx18,cx19,cx20]
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
                for num in range(20):
                    #id.insert(num,num)
                    num=int(id)
                    cy[num] = cy
                    cx[num] =cx
                    num +=1
                
            if cy[8] > cy[7]:
                if "Index Finger" in Fing:
                    Fing.remove("Index Finger")
            if cy[8] < cy[7]:
                if "Index Finger" not in Fing:
                    Fing.insert(1,"Index Finger")
            if cy[12] > cy[11]:
                if "Middle Finger" in Fing:
                    Fing.remove("Middle Finger")
            if cy[12] < cy[11]:
                if "Middle Finger" not in Fing:
                    Fing.insert(2,"Middle Finger")
            if cy[16] > cy[15]:
                if "Ring Finger" in Fing:
                    Fing.remove("Ring Finger")
            if cy[16] < cy[15]:
                if "Ring Finger" not in Fing:
                    Fing.insert(3,"Ring Finger")
            if cy[20] > cy[19]:
                if "Little Finger" in Fing:
                    Fing.remove("Little Finger")
            if cy[20] < cy[19]:
                if "Little Finger" not in Fing:
                    Fing.insert(4,"Little Finger")
            if cx[17] > cx[5]:
                if cx[4] > cx[3]:
                    if "Thump" in Fing:
                        Fing.remove("Thump")
                if cx[4] < cx[3]:
                    if "Thump" not in Fing:
                        Fing.insert(0,"Thump")
            if cx[17] < cx[5]:
                if cx[4] < cx[3]:
                    if "Thump" in Fing:
                        Fing.remove("Thump")
                if cx[4] > cx[3]:
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