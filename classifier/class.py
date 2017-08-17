import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('cascade.xml')

#cap = cv2.VideoCapture(0)
img = cv2.imread('img1.jpg')
#while(True):
     #Capture frame-by-frame
      #ret, img = cap.read()
img = cv2.resize(img, (150,300))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.3,5)
print faces
for (x,y,w,h) in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	
    # if cv2.waitKey(1) & 0xFF == ord('q'):
     #   break
cv2.imshow('img',img)
#cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

