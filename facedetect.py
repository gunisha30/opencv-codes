import cv2
img=cv2.imread("C:\\Users\\hp1\\Pictures\\30.07.18\\facedetect.jpg")
faces1 = cv2.CascadeClassifier("C:\\Users\\hp1\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces2=faces1.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
for a,b,c,d in faces2:
    img=cv2.rectangle(img,(a,b),(a+c,b+d),(0,255,0),3)
cv2.imshow("ab",img)
