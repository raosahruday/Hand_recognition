import cv2
import mediapipe as mp
import pyautogui
x1=y1=x2=y2=x3=y3=x4=y4=0
webcam=cv2.VideoCapture(0)
my_hands=mp.solutions.hands.Hands() #objects to capture our hand broke to draw points
drawing_utils=mp.solutions.drawing_utils
while True:
    _, image=webcam.read()
    image=cv2.flip(image,1)
    frame_height,frame_width,_=image.shape
    cv2.imshow("Hand volume control",image)
    rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output=my_hands.process(rgb_image)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            landmarks=hand.landmark
            drawing_utils.draw_landmarks(image,hand)
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                if id==12:
                    cv2.circle(img=image,center=(x,y),radius=8,color=(255,0,0),thickness=3)
                    x3=x
                    y3=y
                if id==4: #thumb
                    cv2.circle(img=image,center=(x,y),radius=8,color=(0,255,255),thickness=3)
                    x1=x
                    y1=y
                    dist_tab=((x1-x3)**2+(y1-y3)**2)**(0.5)
                if id==8: #fore finger
                    cv2.circle(img=image,center=(x,y),radius=8,color=(0,0,255),thickness=3)
                    x2=x
                    y2=y
                    dist_vol=((x2-x3)**2+(y2-y3)**2)**(0.5)
                    cv2.line(image,(x3,y3),(x2,y2),(0,255,0),thickness=10)
                if id==20:
                    cv2.circle(img=image,center=(x,y),radius=8,color=(0,0,255),thickness=3)
                    x4=x
                    y4=y
                    dist_new=((x2-x4)**2+(y2-y4)**2)**(0.5)
        if dist_tab>150:
            pyautogui.hotkey('ctrl','tab')
        if dist_vol<100 and dist_vol>40:
            pyautogui.press('volumedown')
        elif dist_vol>100:
            pyautogui.press('volumeup')
        if dist_new>200:
            pyautogui.hotkey('ctrl','t')
    cv2.imshow("Hand volume control",image)
    key=cv2.waitKey(10)
    if key==27:
        break
webcam.release()
cv2.destroyAllWindows()
