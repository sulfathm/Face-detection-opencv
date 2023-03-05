# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:46:06 2023

@author: user pc
"""

import cv2

cam = cv2.VideoCapture('http://192.168.43.1:4747/video')
# cam = cv2.VideoCapture(0)

while True:
    check, frame = cam.read()

    cv2.imshow('video', frame)

    key = cv2.waitKey(1)
    if key ==27 :
        break

cam.release()
cv2.destroyAllWindows()