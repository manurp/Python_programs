import cv2
import numpy as np

img = cv2.imread('apple.jpeg', cv2.IMREAD_COLOR)

# Random values are taken here


# extract a pixel
px = img[55, 55]
print(px)

# Region of interest
roi = img[300:750, 100:150]
# print(roi)

img[300:750, 100:150] = [153, 125, 96]

# Here the dimension and lhs and rhs should be same
img[100:350, 600:675] = img[200:450, 625:700]


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
