import cv2
import numpy as np
import os
def partA():
    vidcap = cv2.VideoCapture("..\\Videos\\RoseBloom.mp4")
    vidcap.set(cv2.CAP_PROP_POS_MSEC,6000)      
    success,image = vidcap.read()
    if success:
        cv2.imwrite("..\\Generated\\frame_as_6.jpg", image)          
def partB():
    image = cv2.imread("..\\Generated\\frame_as_6.jpg")
    
    r = image.copy()
    r[:, :, 0] = 0
    r[:, :, 1] = 0

    cv2.imwrite("..\\Generated\\frame_as_6_red.jpg", r)
    

partA()
partB()
