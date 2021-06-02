import cv2
import numpy as np
import math # for math.floor

# Read image 
img = cv2.imread("lenna.jpg", cv2.IMREAD_GRAYSCALE) # (512, 512)
cv2.imshow("origianl", img)
(h, w) = img.shape[:2]

# Crop image into 8*8 patches
patches = [] # patches
for i in range(0, img.shape[0], 8):
    for j in range(0, img.shape[1], 8):
        patches.append(img[i:i+8 ,j:j+8])

# Compute the DCT (discrete cosine transform) of each block. This is implemented in popular packages such as Matlab.
dct_list = []

for p in patches:
    patch = cv2.dct(np.float32(p))

    # Round the coefficient value
    # for i in range(8):
    #     for j in range(8):
    #         patch[i ,j] = round(patch[i ,j])
    
    dct_list.append(np.int16(patch))

# Decode JPEG
img_new = np.zeros((h, w), np.uint8)
for i in range(0, img.shape[0], 8):
    for j in range(0, img.shape[1], 8):
        img_new[i:i+8 ,j:j+8] = np.uint8(cv2.idct(np.float32(dct_list.pop(0))))
cv2.imshow("img_decode", img_new)

cv2.waitKey(0)