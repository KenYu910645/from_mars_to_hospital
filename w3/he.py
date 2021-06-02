# Implement a histogram equalization function
import cv2
import numpy as np
import math # for math.floor
from matplotlib import pyplot as plt

# Read image 
img = cv2.imread("lenna.jpg", cv2.IMREAD_GRAYSCALE) # (512, 512)
(h, w) = img.shape[:2]
PIXEL_NUM = h*w
cv2.imshow("original", img)

# Historgram Equlization with built-in function
img_eq = cv2.equalizeHist(img)
cv2.imshow("HE_built_in", img_eq)

f = plt.figure(1)
plt.hist(img_eq.ravel(),256,[0,256])
f.show()

# Historgram Equlization with self-implementation
hist = cv2.calcHist([img],[0],None,[256],[0,256])
he_map = {} # {old_gray_value : new_gray_value, .....}
hist_idx = 0
balance = 0
for gray_value in range(256):
    balance += PIXEL_NUM / 256
    # print("Balance = " + str(balance))
    while balance > 0: # Need a gray value to fill in
        if hist_idx > 255:
            break
        he_map[hist_idx] = gray_value
        balance -= int(hist[hist_idx])
        hist_idx += 1

img_new = np.zeros((h, w), np.uint8)
for i in range(h):
    for j in range(w):
        img_new[i, j] = he_map[img[i, j]]
cv2.imshow("HE_homemade", img_new)

g = plt.figure(2)
plt.hist(img_new.ravel(),256,[0,256])
g.show()

# Keep plot alive
input()