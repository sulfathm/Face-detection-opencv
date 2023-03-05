# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:40:34 2023

@author: user pc
"""

import cv2

# black ands white (grey scale)

img = cv2.imread("fish.jpg",0)

#  save image

status= cv2.imwrite('greenspottedfish.png',img)

cv2.imshow('data',img)

cv2.waitKey(0)
cv2.destroyAllWindows()