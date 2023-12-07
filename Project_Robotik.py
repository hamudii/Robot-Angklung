import mediapipe as mp
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject 
import numpy as np
import time
import serial

vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = HandDetector(maxHands=1, detectionCon=1)
arduino = serial.Serial('COM5', 9600)


if (vid.isOpened() == False):
    print("Error opening the video file")

start = time.time()
isSend = False
fingers2 = ''
hasil = ''

while(vid.isOpened()):
    ret, frame = vid.read()
    if (time.time()-start) > 0.59:
        isSend = False
        start = time.time()
    if ret == True:
        frame = detector.findHands(frame)
        lmList, bbox = detector.findPosition(frame)
        if lmList :
            fingers = detector.fingersUp()
            fingers2=str(fingers[0])+str(fingers[1])+str(fingers[2])+str(fingers[3])+str(fingers[4])
            if isSend:
                continue
            if fingers2=='10000':
                arduino.write(b'1')
                hasil = 'do'
                isSend = True
            elif fingers2=='11000':
                arduino.write(b'2')
                hasil = 're'
                isSend = True
            elif fingers2=='11100':
                arduino.write(b'3')
                hasil = 'mi'
                isSend = True
            elif fingers2=='11110':
                arduino.write(b'4')
                hasil = 'fa'
                isSend = True
            elif fingers2=='11111':
                arduino.write(b'5')
                hasil = 'so'
                isSend = True
            elif fingers2=='01111':
                arduino.write(b'6')
                hasil = 'la'
                isSend = True
            elif fingers2=='00111':
                arduino.write(b'7')
                hasil = 'si'
                isSend = True
            elif fingers2=='00011':
                arduino.write(b'8')
                hasil = 'do!'
                isSend = True
            else:
                result = ''
                hasil = ''
        cv2.putText(frame, hasil, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        cv2.imshow("Hasil", frame)
        
    else:
        break
    k = cv2.waitKey(20)
    if k == 27:
        break   
vid.release()
cv2.destroyAllWindows()
