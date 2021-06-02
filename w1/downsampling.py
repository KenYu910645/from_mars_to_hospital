# For  every 3×3 times 3×3 block of the image (without overlapping),
# replace  all corresponding 9 pixels by their average. This operation simulates 
# reducing the image spatial resolution. Repeat this for 5×5 times 5×5  blocks and 
# 7×7 times 7×7 blocks. If you are using Matlab, 
# investigate  simple command lines to do this important operation.

import cv2
import numpy as np
import math# for math.ceil

S = 3 # Downsampling size, 3x3, 5x5, 7x7

# Read image 
img = cv2.imread("lenna.png", cv2.IMREAD_GRAYSCALE) # (512, 512, 3)
cv2.imshow("original", img)
(h, w) = img.shape[:2]

# padding # (top, bottom, left, right)
img_pad = cv2.copyMakeBorder(img, 0, S, S, 0, cv2.BORDER_REPLICATE)

# New output image
img_out = np.zeros((math.ceil(h/S), math.ceil(w/S)), np.uint8)

# Access pixel
for i in range(0, img.shape[0], S): # Stride is S
    for j in range(0, img.shape[1], S): # Stride is S
        block_list = [] # Record gray value's in the block
        for ii in range(i, i+S):
            for jj in range(j, j+S):
                block_list.append(img_pad[ii, jj])
        img_out[math.floor(i/S) ,math.floor(j/S)] = max(block_list)

# Show image
cv2.imshow("result", img_out)
cv2.waitKey(0)