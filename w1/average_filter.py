# load an image and then  perform a simple spatial 3x3 average of image pixels.
# In other words,  replace the value of every pixel by the average of the values in its 3x3
#  neighborhood. If the pixel is located at (0,0), this means averaging 
#  the values of the pixels at the positions
#  (-1,1), (0,1), (1,1), (-1,0),  (0,0), (1,0), (-1,-1), (0,-1), and (1,-1).
#  Be careful with pixels at the image boundaries. Repeat the process for a 10x10 neighborhood and
#  again for a 20x20 neighborhood. Observe what happens to the image 
#  (we will discuss this in more details in the very near future, about week 3).

import cv2
import numpy as np
import math # for math.floor

FILTER_SIZE = 21 # 3x3, 5x5, 7x7, 21*21
FILTER_SIZE_2 = math.floor(FILTER_SIZE / 2) 

# Read image 
img = cv2.imread("lenna.jpg", cv2.IMREAD_GRAYSCALE) # (512, 512, 3)
(h, w) = img.shape[:2]
cv2.imshow("original", img)

# padding
img_pad = cv2.copyMakeBorder(img, 
                             FILTER_SIZE_2,
                             FILTER_SIZE_2,
                             FILTER_SIZE_2,
                             FILTER_SIZE_2,
                             cv2.BORDER_REPLICATE)

# Access pixels, calcualte img_out
img_new = np.zeros((h, w), np.uint8)
for i in range(h):
    for j in range(w):
        # Get filter values
        filter_values = []
        for ii in range(FILTER_SIZE):
            for jj in range(FILTER_SIZE):
                filter_values.append(img_pad[i+ii, j+jj])
        img_new[i ,j] = int( sum(filter_values) / len(filter_values) )
cv2.imshow("result", img_new)

# Show image
cv2.waitKey(0)