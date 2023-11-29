import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import os 

for i in range(5501,5923):
    img = cv2.imread("C:\PBL\Craw\train\ " + str(i) + ".jpg")
    cv2.imwrite("C:\PBL\Craw\test\ " + str(i) + ".jpg",img)