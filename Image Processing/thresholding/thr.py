import cv2
import numpy as np

# take a text image in darker condition, here the image is not that ideal
img = cv2.imread('../images/page.jpg')
grayScaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('original', img)

# The value '50' -> 2nd parameter changes according to the image
retval, threshold = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

retval1, threshold1 = cv2.threshold(grayScaled, 40, 255, cv2.THRESH_BINARY)

# Guassian thresholding -> need to look into the parameters
guas = cv2.adaptiveThreshold(grayScaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

# otsu thresholding
retval2, otsu = cv2.threshold(grayScaled, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('thresholded', threshold)
cv2.imshow('Gray scale threshold', threshold1)
cv2.imshow('Guassian threshold', guas)
cv2.imshow('Otsu threshold', otsu)


cv2.waitKey(0)
cv2.destroyAllWindows()
