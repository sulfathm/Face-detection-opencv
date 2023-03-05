# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:49:10 2023

@author: user pc
"""

# Import OpenCV module  
import cv2  
# Import pyplot from matplotlib as pltd  
from matplotlib import pyplot as pltd  
# Opening the image from files  
imaging = cv2.imread("clock.jpg")  
# Altering properties of image with cv2  
img_gray = cv2.cvtColor(imaging, cv2.COLOR_BGR2GRAY)  
imaging_rgb = cv2.cvtColor(imaging, cv2.COLOR_BGR2RGB)  
# Plotting image with subplot() from plt  
pltd.subplot(1, 1, 1)  
# Displaying image in the output  
pltd.imshow(imaging_rgb)  
pltd.show()  