# Implement the Hough transform to detect circles.
import cv2
import numpy as np
import math # for math.floor
from matplotlib import pyplot as plt

# Read image 
img = cv2.imread("lane.jpg", cv2.IMREAD_GRAYSCALE) # (512, 512)
(h, w) = img.shape[:2]
cv2.imshow("original", img)

# GaussianBlur
kernel_size = 7
img_blur = cv2.GaussianBlur(img,(kernel_size, kernel_size), 0)
# cv2.imshow('gaussian_blur', img_blur)

# Canny edge detection
img_canny = cv2.Canny(img_blur, 30, 150)
cv2.imshow('Canny', img_canny)

# Opencv2 Hough Transform

# 
circles = cv2.HoughCircles(img_canny,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
                            
circles = np.uint16(np.around(circles))
img_out = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img_out,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img_out,(i[0],i[1]),2,(0,0,255),3)
cv2.imshow('detected circles',img_out)


# Keep plot alive
cv2.waitKey(0)