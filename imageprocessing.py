import cv2
import numpy as np
import os
import csv
img1=cv2.imread('..\\Images\\bird.jpg',1)
img2=cv2.imread('..\\Images\\cat.jpg',1)
img3=cv2.imread('..\\Images\\flowers.jpg',1)
img4=cv2.imread('..\\Images\\horse.jpg',1)
def partA(img,s):
    height, width, ch= img.shape
    color = img[(height//2), (width//2)]
    s1=os.path.basename(s)
    b=[s1,height,width,ch,color[0],color[1],color[2]]
    with open('..\\Generated\\stats.csv','a') as csvFile:
        wr=csv.writer(csvFile)
        wr.writerow(b)
    csvFile.close()
def partB(img):
    img[:,:,0]=0
    img[:,:,1]=0
    cv2.imwrite("..\\Generated\\cat_red.jpg",img)
def partC(img):
    alpha = np.zeros([img.shape[0],img.shape[1],1], dtype=np.uint8) + 128
    bg = np.dstack((img,alpha))
    cv2.imwrite("..\\Generated\\flowers_alpha.png",bg)

def partD(img):
    height, width, ch= img.shape
    for i in range(height):
        for j in range(width):
            b,g,r=img[i,j]
            img[i,j]=(0.3*r)+(0.59*g)+(0.11*b)
    cv2.imwrite("..\\Generated\\horse_gray.jpg",img) 
partA(img1,'bird.jpg')
partA(img2,'cat.jpg')
partA(img3,'flowers.jpg')
partA(img4,'horse.jpg')
partB(img2)
partC(img3)
partD(img4)
