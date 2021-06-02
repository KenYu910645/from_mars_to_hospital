# Implement the non-local means algorithm.
# Try different window sizes. 
# Add different levels of noise and see the influence of it in the need for larger or 
# smaller neighborhoods.
import cv2
import numpy as np
import math
import time

FILTER_SIZE = 8 # 8x8
SEARCH_SIZE = 24 #
H = 15 # 

# Read image 
img = cv2.imread("lenna.jpg", cv2.IMREAD_GRAYSCALE) # (512, 512)
cv2.imshow("original", img)
(h, w) = img.shape[:2]

# Build-in function 
img_build_in = cv2.fastNlMeansDenoising(img,None,H,FILTER_SIZE,SEARCH_SIZE)
cv2.imshow("img_build_in", img_build_in)

# Access pixels
img_new = np.zeros((h, w), np.uint8)
for i in range(0, h, FILTER_SIZE):
    for j in range(0, w, FILTER_SIZE):
        # Debugging
        img_draw = img.copy()
        cv2.rectangle(img_draw, (i, j), (i+FILTER_SIZE, j+FILTER_SIZE), (0, 255, 0), 2)

        # (i ,j) is left-upper coner of filter region
        # Get search areas
        search_areas = [] # [img1, img2, img3, .....]
        s_2 = int(SEARCH_SIZE/(FILTER_SIZE*2))*FILTER_SIZE # (24/8)*0.5 * 8
        for ii in range(i - s_2, i + s_2 + FILTER_SIZE, FILTER_SIZE):
            for jj in range(j - s_2, j + s_2 + FILTER_SIZE, FILTER_SIZE):
                # (ii ,jj) is left-upper corner of every searching region
                if ii < 0 or jj < 0 or ii >= h or jj >= w:
                    pass
                    # print("Ignore : " + str((ii, jj)))
                else:
                    # print("Accept : " + str((ii, jj)))
                    search_areas.append(img[ii:ii+FILTER_SIZE, jj:jj+FILTER_SIZE])
                    cv2.rectangle(img_draw, (ii, jj), (ii+FILTER_SIZE, jj+FILTER_SIZE), (0, 128, 0), 1)
        
        # Get weight of each region
        weight_list = []
        for search_area in search_areas:
            mse = ((img[i:i+FILTER_SIZE, j:j+FILTER_SIZE] - search_area)**2).mean(axis=None)
            weight_list.append(math.exp(-mse/(H**2)))
        
        # normalize weight
        weight_sum = sum(weight_list)
        for ii in range(len(weight_list)):
            weight_list[ii] = weight_list[ii] / weight_sum
        
        # Calculate every pixel in this region 
        for ii in range(FILTER_SIZE):
            for jj in range(FILTER_SIZE):
                pixel_acc = 0.0
                for idx in range(len(search_areas)):
                    pixel_acc += search_areas[idx][ii ,jj] * weight_list[idx]
                # print(pixel_acc)
                img_new[i+ii, j+jj] = int(pixel_acc)

        # key = cv2.waitKey()
        # if key == ord('q') or key == 27: # Esc
        #     continue
        cv2.imshow("debbug", img_draw)
        cv2.waitKey(100)

cv2.imshow("non_local_filter", img_new)
# Show image
cv2.waitKey(0)