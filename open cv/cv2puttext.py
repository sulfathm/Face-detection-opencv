# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:18:27 2023

@author: user pc
"""

import cv2

image=cv2.imread('waterfall.jpg',1)

position=(800,300)
cv2.putText(
    image,# image on  which text is written
    "python Example", #text
    position, # position at which writing has to start
    cv2.FONT_HERSHEY_SIMPLEX, #font family
    1, # font size
    (0,0,255,255), # font color
    3) # font stroke


cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyallwindows()