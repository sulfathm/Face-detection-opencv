# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 12:12:51 2023

@author: user pc
"""

import cv2

#cam = cv2.VideoCapture('http://192.168.43.1:4747/video')
cam = cv2.VideoCapture(0)

while True:
    check, frame = cam.read()
    cv2.imshow('video', frame)
    e=0
    for i in range(0,10):
        e=e+i
        c=str(i)
        cv2.imwrite('New folder/'+c+'.Jpg',frame)
        if (e==10):
            cam.release()
            cv2.destroyAllWindows()
            #key = cv2.waitKey(0)
            #if key == 27:
                #break
    
    
#cv2.waitKey(30)
#cam.release()
#cv2.destroyAllWindows()