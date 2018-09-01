# Image arithmetics and Logic

import cv2
import numpy as np

# img1 and img2 are of same size
img1 = cv2.imread('../images/3D-Matplotlib.png')
img2 = cv2.imread('../images/mainsvmimage.png')

# img3 is smaller than img1
img3 = cv2.imread('../images/mainlogo.png')

# add = img1 + img2

# Here the individual components of the pixel are added -->(b,g,r)1 + (b,g,r)2
add = cv2.add(img1, img2)

# Last parameter --> 0 is the gamma value
# dst = src1*alpha + src2*beta + gamma;
# alpha --> 2nd param(0.6)
# beta --> 4th param(0.4)
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Image 3', img3)

cv2.imshow('Add', add)
cv2.imshow('Weighted', weighted)

cv2.waitKey(0)
cv2.destroyAllWindows()

rows, cols, channels = img3.shape
roi = img2[0:rows, 0:cols]

img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

# Pixel value above 220(2nd param) is converted to 255(3rd param) due to the last parameter it is inverted
ret, mask = cv2.threshold(img3gray, 220, 255, cv2.THRESH_BINARY_INV)

# cv2.imshow('mask', mask)
# cv2.imshow('ret', ret)

mask_inv = cv2.bitwise_not(mask)
img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)
dst = cv2.add(img2_bg, img3_fg)
img2[0:rows, 0:cols] = dst

cv2.imshow('background', img2_bg)
cv2.imshow('foreground', img3_fg)
cv2.imshow('Mask Inverse', mask_inv)
cv2.imshow('New Image 2', img2)


cv2.waitKey(0)
cv2.destroyAllWindows()
