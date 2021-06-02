# Rotate the image by 45 and 90 degrees

import cv2
import numpy as np

# Read image 
img = cv2.imread("lenna.png", cv2.IMREAD_GRAYSCALE) # (512, 512, 3)
cv2.imshow("origianl", img)

# Rotate 90 degree
img_rot = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("rotate 90", img_rot)

# Rotate 45 degree
(h, w) = img.shape[:2]
center = (w / 2, h / 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
img_rot = cv2.warpAffine(img, M, (w, h))
cv2.imshow("rotate 45", img_rot)

# Show image
cv2.waitKey(0)
