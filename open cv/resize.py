# import cv2
# import numpy as np
 
#importing the opencv module  
import cv2  
# using imread('path') and 1 denotes read as  color image  
img = cv2.imread('waterfall.jpg',1)  
print(img.shape)
img_resized=cv2.resize(img, (500, 500),  
               interpolation = cv2.INTER_NEAREST)
print(img_resized.shape)
cv2.imshow("Resized",img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
