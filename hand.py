import cv2 as cv
from cvzone import HandTrackingModule
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 250)
video = cv.VideoCapture(0)
detector = HandTrackingModule.HandDetector()

prev_num_hands = -1
count = 0

while True:
    isTrue, frame = video.read()
    hands, img = detector.findHands(frame)
    
    num_hands = len(hands)
    if count == 0 and num_hands == 2:
        text = "Engine is started you can drive. Happy Journey"
        engine.say(text)
        engine.runAndWait()
        count+=1
    if count == 0:
        text = "Place your hands on the steering to start the engine"
        engine.say(text)
        engine.runAndWait()

    if count>0:
        if num_hands != prev_num_hands:
            prev_num_hands = num_hands  
        
            if num_hands == 2:
                text = "You can drive at the max speed"
                engine.say(text)
                engine.runAndWait()
            elif num_hands == 1:
                text = "You can drive at max speed of 30Km/h"
                engine.say(text)
                engine.runAndWait()
            elif num_hands == 0:
                text = "There are no hands on the steering. Brakes are being applied"
                engine.say(text)
                engine.runAndWait()
    
    cv.imshow("Hands Detected", img)
    
    key = cv.waitKey(10)
    if key & 0xFF == ord("d"):
        break

video.release()
cv.destroyAllWindows()
