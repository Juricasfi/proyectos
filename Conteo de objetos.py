# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:12:27 2020
@author: juric
"""
import cv2
import numpy as np
video = cv2.VideoCapture(0)
i = 0
while True:
  ret, cap = video.read()
  if ret == False: break
  gris = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
  
  _, binarizada = cv2.threshold(gris,100,255,cv2.THRESH_BINARY_INV)

  kernel =cv2.getStructuringElement(cv2.MORPH_RECT,(8,8))
  eroded = cv2.erode(binarizada,kernel)
  dilated = cv2.dilate(eroded,kernel)

  contornos, y = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cv2.drawContours(cap, contornos, -1, (0,0,255), 3)

#cv2.contourArea(contornos)
#comparar el tamaño, si es muy pequeño no lo lee y si es muy grande tampoco
  
  #bordes=cv2.Canny(cap,10,100)  detecta los bordes y pone todo negro menos los bordes 

  font = cv2.FONT_HERSHEY_SIMPLEX
  mensaje = 'Numero de Objetos:' + str(len(contornos))
  cv2.putText(cap,mensaje,(10,50),font,0.75,
    (255,0,0),2,cv2.LINE_AA)
  
  cv2.imshow('camara',cap)
          
  if cv2.waitKey(30) & 0xFF == ord ('q'):
    break
video.release()
