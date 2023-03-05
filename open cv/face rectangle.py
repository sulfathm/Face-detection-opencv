# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 19:55:26 2023

@author: user pc
"""

import cv2
x=0
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap= cv2.VideoCapture(0)

while True:
    check, img=cap.read()

# img=cv2.imread('faces.JFIF')

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale (gray,1.1,4)

    for (x , y, w ,h ) in faces:
         x=x+1
         d=str(x)
         cv2.rectangle(img,(x,y),(x+w , y+h) , (255,0,0),2)
         
         
         status= cv2.imwrite('Facedetect/'+d+'.png',img)
         
    
    
    cv2.imshow('img',gray)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
    
cap.release()