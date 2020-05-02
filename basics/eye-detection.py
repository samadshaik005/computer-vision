import numpy as np
import cv2

face_classifier=cv2.CascadeClassifier('./Haarcascades/haarcascade_frontalface_default.xml')
eye_classifier=cv2.CascadeClassifier('./Haarcascades/haarcascade_eye.xml')

image=cv2.imread('./image_examples/Trump.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


faces=face_classifier.detectMultiScale(gray,1.3,5)
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,255),2)
    #cv2.imshow('img',image)
    #cv2.waitKey(0)

    roy_gray=gray[y:y+h,x:x+w]
    roy_color=image[y:y+h,x:x+w]
    eyes=eye_classifier.detectMultiScale(roy_gray)
    for(ex,ey,ew,eh) in eyes:
    	cv2.rectangle(roy_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
    	cv2.imshow('image',image)
    	cv2.waitKey(0)
cv2.destroyAllWindows()