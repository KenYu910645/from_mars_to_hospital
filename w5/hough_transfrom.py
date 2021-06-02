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

# Hough transform with built-in function
rho = 1
theta = np.pi/180
threshold = 1
min_line_length = 10
max_line_gap = 1
lines = cv2.HoughLinesP(img_canny, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

# Draw detected line on image
img_out = np.zeros((h, w), np.uint8)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img_out, (x1, y1), (x2, y2), (255,0,0), 2)
cv2.imshow('Detected_line_cv2', img_out)
 
d = math.sqrt(h**2 + w**2) # diagonal length of image
acc_matrix = np.zeros( (int(2*d/rho + 1), int(2*np.pi/theta)) ,np.uint8)
for y in range(h):
    for x in range(w):
        if img_canny[y, x] == 255: # It's a edge point
            for step in range(int(2*np.pi/theta)):
                r = x*math.cos(step*theta) + y*math.sin(step*theta)
                # print((int(r / rho), step))
                acc_matrix[int(r/rho) + int(d/rho), step] += 1 # vote
cv2.imshow('acc_matrix', acc_matrix)

# Draw detected line on image
THRES = 150
E = 0.00000001 # avoid zero division
img_out = img_canny.copy()# np.zeros((h, w), np.uint8)
count = 0
for i in range(acc_matrix.shape[0]):
    for j in range(acc_matrix.shape[1]):
        if acc_matrix[i, j] > THRES:
            x0 = 0
            x1 = h
            y0 = ( (i*rho - d) - (x0*math.cos(j*theta)) ) / (math.sin(j*theta) + E)
            y1 = ( (i*rho - d) - (x1*math.cos(j*theta)) ) / (math.sin(j*theta) + E)
            y2 = 0
            y3 = w
            x2 = ( (i*rho - d) - (y2*math.sin(j*theta)) ) / (math.cos(j*theta) + E)
            x3 = ( (i*rho - d) - (y3*math.sin(j*theta)) ) / (math.cos(j*theta) + E)
            l = [(int(x0), int(y0)), (int(x1), int(y1)), (int(x2), int(y2)), (int(x3), int(y3))]
            l_good = []
            for ii in l:
                if (ii[0] <= h and ii[0] >= 0) and (ii[1] <= w and ii[1] >= 0):
                    l_good.append(ii)
            print(l_good)
            count += 1
            cv2.line(img_out, l_good[0], l_good[1], (255,0,0), 2)
print("Totoal line  = " + str(count))
cv2.imshow('Detected_line_implement', img_out)

# Keep plot alive
cv2.waitKey(0)