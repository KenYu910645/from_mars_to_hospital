# Implement a median filter. 
# Add different levels and types of noise to an image and experiment with different 
# sizes of support for the median filter. 
# As before, compare your implementation with Matlab’s.
import cv2
import numpy as np
import math # for math.floor
import statistics # for statistics.median()

FILTER_SIZE = 3 # 3x3, 5x5, 7x7
FILTER_SIZE_2 = math.floor(FILTER_SIZE / 2) 
# Read image 
img = cv2.imread("lenna.jpg", cv2.IMREAD_GRAYSCALE) # (512, 512)
cv2.imshow("original", img)
(h, w) = img.shape[:2]

# padding
img_pad = cv2.copyMakeBorder(img, 
                             FILTER_SIZE_2,
                             FILTER_SIZE_2,
                             FILTER_SIZE_2,
                             FILTER_SIZE_2,
                             cv2.BORDER_REPLICATE)

# Access pixels
img_new = np.zeros((h, w), np.uint8)
for i in range(h):
    for j in range(w):
        # Get filter values
        filter_values = []
        for ii in range(FILTER_SIZE):
            for jj in range(FILTER_SIZE):
                filter_values.append(img_pad[i+ii, j+jj])
        img_new[i, j] = statistics.median(filter_values)
cv2.imshow("median_filter_self", img_new)

# Opencv2 Build-in median filter
img_cv2 = cv2.medianBlur(img, FILTER_SIZE)
cv2.imshow("median_filter_cv2", img_cv2)


# Show image
cv2.waitKey(0)