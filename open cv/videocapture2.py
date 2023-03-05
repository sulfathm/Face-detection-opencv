# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 12:36:20 2023

@author: user pc
"""

import cv2
cam=cv2.VideoCapture(0)
while True:
    check,frame=cam.read()
    #cv2.imshow('video',frame)
    e=0
    for i in range(0,10):
        e=e+i
        c=str(i)
        cv2.imwrite('New folder/'+c+'.jpg',frame)
        cv2.imshow('video',frame)
        if (e==10):
            cam.release()
            cv2.waitKey(0)
            cv2.destroyAllWindows