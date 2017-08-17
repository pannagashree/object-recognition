import numpy as np
import cv2
purse = cv2.CascadeClassifier('cascade.xml')
nail = cv2.CascadeClassifier('nail.xml')

cap = cv2.VideoCapture(0)
#img = cv2.imread('nail.jpg')
while(True):
     #Capture frame-by-frame
     ret, img = cap.read()
     img = cv2.resize(img, (300,500))
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

     purses = purse.detectMultiScale(gray,1.3,3)
     nails = nail.detectMultiScale(gray,1.35,10)
     print purses
     print nails
     for (x,y,w,h) in purses:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
     for (x,y,w,h) in nails:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break
     cv2.imshow('video',img)
cap.release()
#cv2.waitKey(0)
#cv2.destroyAllWindows()

