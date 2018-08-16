import cv2
import numpy as np
import matplotlib.pyplot as plt

# If second parameter is not mentioned the default image reading is the color image
# other things can be used as below
# IMREAD_COLOR  -> 1
# IMREAD_UNCHANGED -> -1
# IMREAD_GRAYSCALE -> 0
# The second parameter can be replaced the constants as mentioned above
img = cv2.imread('apple.jpeg', cv2.IMREAD_GRAYSCALE)

# Uncomment the lines if needed
# plot image using cv2
# cv2.imshow('image', img)  # first parameter -> title
# cv2.waitKey(0)  # press any key to go to next line
# cv2.destroyAllWindows()

# plot image using matplotlib

# Uncomment the lines if needed
# color map here is set as gray
plt.imshow(img, cmap='gray', interpolation='bicubic')
# to plot on that image
# the character 'c' can be changed to get different colors
plt.plot([50, 100], [80, 100], 'c', linewidth=5)  # some random co-ordinates
plt.show()

# To save the image
cv2.imwrite('apple_g.png', img)
