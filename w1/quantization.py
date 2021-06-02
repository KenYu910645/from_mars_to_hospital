# Write a computer program capable of reducing the number of intensity levels 
# in an image from 256 to 2, in integer powers of 2. The desired number of  
# intensity levels needs to be a variable input to your program.

import cv2
import numpy as np
import math # for math.floor

NUM_LEVEL = 8
d = 256/NUM_LEVEL # Divisor

# Read image 
img = cv2.imread("lenna.png", cv2.IMREAD_GRAYSCALE) # (512, 512, 3)

# Access pixels
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i, j] = math.floor(img[i, j] / d) * d # Quantization

# Show image
cv2.imshow("lenna", img)
cv2.waitKey(0)
