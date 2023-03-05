# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:03:31 2023

@author: user pc
"""

import cv2
import matplotlib.pyplot as plt
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.imread("clock.jpg")

 
#img_gray = cv2.cvtColor(imaging, cv2.COLOR_BGR2GRAY)  
imaging_rgb = cv2.cvtColor(cap, cv2.COLOR_BGR2RGB)  
# Plotting image with subplot() from plt  
#plt.subplot(1, 1, 1)  
# Displaying image in the output  
plt.imshow(imaging_rgb)  
plt.show()  