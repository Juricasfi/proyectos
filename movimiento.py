# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:06:47 2020

@author: juric
"""
import cv2
import numpy as np
video = cv2.VideoCapture(0)
i = 0
while True:
  ret, cap = video.read()
  if ret == False: break
  gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
  if i == 25:
    bgGray = gray
  if i > 25:
    dif = cv2.absdiff(gray, bgGray)
    _, th = cv2.threshold(dif, 30, 255, cv2.THRESH_BINARY)
    cv2.imshow('th',th)
    cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
      area = cv2.contourArea(c)
      if area > 500:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(cap, (x,y), (x+w,y+h),(0,255,0),2)
  cv2.imshow('Frame',cap)
  i = i+1
  if cv2.waitKey(30) & 0xFF == ord ('q'):
    break
video.release()

#cv2.contourArea(ht)

