# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:26:45 2020
@author: juric
"""
import cv2
import sys

cas_path = 'haarcascade_frontalface_default.xml' 
face_cascade = cv2.CascadeClassifier(cas_path)

webcam_id = 0
video_capture = cv2.VideoCapture(webcam_id)

if cv2.__version__.startswith('2.4'):
    dmf_flag = cv2.cv.CV_HAAR_SCALE_IMAGE
else:
    dmf_flag = cv2.CASCADE_SCALE_IMAGE
i=0
while True:
    ret, frame = video_capture.read()
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray_image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=dmf_flag
    )
    for (x, y, w, h) in faces:
        cuadrado=cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        if (y>200 or y<130) and (w<50 and w>30):
            font = cv2.FONT_HERSHEY_SIMPLEX
            mensaje = 'Alerta colado'
            cv2.putText(frame,mensaje,(10,80),font, 3,
            (0,0,255),4,cv2.LINE_AA)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()

