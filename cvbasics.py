import cv2
img=cv2.imread("C:\\Users\\hp1\\Pictures\\animals\\abc.jpg")
print(img.shape)
b=cv2.resize(img,(600,600))
cv2.imshow("a",b)
cv2.waitKey(3000)
cv2.destroyAllWindows()





