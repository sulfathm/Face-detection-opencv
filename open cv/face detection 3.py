# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 00:23:50 2023

@author: user pc
"""

import cv2

# read the input image
# img = cv2.imread('milk nutrition comparison.jpg')
cap= cv2.VideoCapture(0)

while True:
    check, img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# read the haarcascade to detect the faces in an image
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# detects faces in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    print('Number of detected faces:', len(faces))

# loop over all detected faces
    if len(faces) > 0:
        for i, (x, y, w, h) in enumerate(faces):
            #position=(800,300)
            
      # To draw a rectangle in a face
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.putText(img, 'Face Detected', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            face = img[y:y + h, x:x + w]
            cv2.imshow("Cropped Face", gray)
            #cv2.imshow('video', frame)
            for (x , y, w ,h ) in faces:
                 x=x+1
                 d=str(x)
                 cv2.rectangle(img,(x,y),(x+w , y+h) , (255,0,0),2)
                 
                 
                 
                 status= cv2.imwrite('Facedetect/'+d+'.png',gray)
                
                #key = cv2.waitKey(1)
                #if key == 27:
                    #break
      #print(f"face{i}.jpg is saved")
 
# display the image with detected faces
                 cv2.imshow("image", face)

                 key = cv2.waitKey(1)
                 if key == 27:
                     break
                
                
                 if c in face:
                     break
cv2.waitKey(0)                   
cv2.destroyAllWindows()