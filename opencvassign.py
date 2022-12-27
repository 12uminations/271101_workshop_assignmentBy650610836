#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

Nfing = 5
Fing=["Thump", "Index Finger", "Middle Finger", "Ring Finger", "Pinky"]
cyX=[None]*21
cxX=[None]*21
idX =[None]*21
num=0
def Th():
    if "Thump" in Fing:
        Fing.remove("Thump")
def RTh():
    if "Thump" not in Fing:
        Fing.insert(0,"Thump")
def In():
    if "Index Finger" in Fing:
        Fing.remove("Index Finger")
def RIn():
    if "Index Finger" not in Fing:
        Fing.insert(1,"Index Finger")
def Mi():
    if "Middle Finger" in Fing:
        Fing.remove("Middle Finger")
def RMi():
    if "Middle Finger" not in Fing:
        Fing.insert(2,"Middle Finger")
def Ri():
    if "Ring Finger" in Fing:
        Fing.remove("Ring Finger")
def RRi():
    if "Ring Finger" not in Fing:
        Fing.insert(3,"Ring Finger")
def Li():
    if "Pinky" in Fing:
        Fing.remove("Pinky")
def RLi():
    if "Pinky" not in Fing:
        Fing.insert(4,"Pinky")

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
                for num in range(21):
                    if id==num:
                        idX[num] = int(id)
                        cyX[num] = cy
                        cxX[num] = cx
                    num +=1
            
            #normal case *********************************************************
            if cyX[0] > cyX[5]:
                if cyX[8] > cyX[7]:
                    In()
                if cyX[8] < cyX[7]:
                    RIn()
                if cyX[12] > cyX[11]:
                    Mi()
                if cyX[12] < cyX[11]:
                    RMi()
                if cyX[16] > cyX[15]:
                    Ri()
                if cyX[16] < cyX[15]:
                    RRi()
                if cyX[20] > cyX[19]:
                    Li()
                if cyX[20] < cyX[19]:
                    RLi()
            #Thump x axis *********************************************************
            if cxX[17] > cxX[5]: 
                if cxX[4] > cxX[3]:
                    Th()
                if cxX[4] < cxX[3]:
                    RTh()
            if cxX[17] < cxX[5]:
                if cxX[4] < cxX[3]:
                    Th()
                if cxX[4] > cxX[3]:
                    RTh()
            #If hand point down *********************************************************
            if ((cyX[0] < cyX[17]) and cyX[17] > cyX[5]):
                if cyX[8] < cyX[7]:
                    In()
                if cyX[8] > cyX[7]:
                    RIn()
                if cyX[12] < cyX[11]:
                    Mi()
                if cyX[12] > cyX[11]:
                    RMi()
                if cyX[16] < cyX[15]:
                    Ri()
                if cyX[16] > cyX[15]:
                    RRi()
                if cyX[20] < cyX[19]:
                    Li()
                if cyX[20] > cyX[19]:
                    RLi()
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