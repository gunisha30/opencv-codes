import cv2
import numpy as np

cap = cv2.VideoCapture("..\\Videos\\Gargiq1.mp4")
while True:
    ret, frame = cap.read()
    if (ret is False):
        break
    roi=frame[100:195, 170:450]
    rows, cols, _ =roi.shape
    roigr=cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    #roigr=cv2.GaussianBlur(roigr, (7,7) ,0) 
    
    _, thresh= cv2.threshold(roigr, 100,255, cv2.THRESH_BINARY)
    contours, _= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for c in contours:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(roi, (x,y), (x+w, y+h),(255,0,0), 2)
        cv2.line(roi, (x+ int(w/2), 0), (x+ int(w/2), rows), (0,255,0) , 2)
        cv2.line(roi, (0, y+int(h/2)), (cols, y+ int(h/2)), (0,255,0) , 2)
        #cv2.drawContours(roi, [c], -1, (0,0,255), 2)
        break

    cv2.imshow("f1",thresh)
    cv2.imshow("f",roi)
    key=cv2.waitKey(30)
    if (key==27):
      break

cv2.destroyAllWindows()
