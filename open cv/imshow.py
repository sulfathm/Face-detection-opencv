# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:40:34 2023

@author: user pc
"""

import cv2

# black and white (grey scale)

img = cv2.imread("fish.jpg",1)

cv2.imshow('Data',img)

cv2.waitKey(0)

# cv2.waitkey(2000)

cv2.destroyallwindows()