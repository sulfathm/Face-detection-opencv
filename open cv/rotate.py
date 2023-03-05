# -*- coding: utf-8 -*- 
"""
Created on Thu Feb  9 11:13:07 2023

@author: user pc
"""

import cv2
# import numpy as np
 
#importing the opencv module  
# import cv2  
# using imread('path') and 1 denotes read as  color image  
img = cv2.imread('waterfall.jpg',1)  
print(img.shape)

img_resized=cv2.resize(img, (500, 500),  
               interpolation = cv2.INTER_NEAREST)
print(img_resized.shape)

image=cv2.rotate(img_resized,cv2.ROTATE_90_COUNTERCLOCKWISE)
status= cv2.imwrite("rotated image.png",image)
cv2.imshow("img",image)
cv2.waitKey(0)
cv2.destroyAllWindows()