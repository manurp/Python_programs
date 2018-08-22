import cv2
import numpy as np

# The drawing on the image is random
img = cv2.imread('apple.jpeg', cv2.IMREAD_COLOR)

# The co-ordinates of all the drawings should change according to the image used

# draw line on the image 'img'.
# The second and third parameter specfies the start and end co-ordinate
# The color is given by (b,g,r)
# The last parameter(15) is the line width
cv2.line(img, (0, 0), (1450, 650), (25, 255, 255), 15)

cv2.rectangle(img, (115, 265), (200, 650), (0, 32, 16), 5)

# The second parameter is the center of the circle
# The third one is the radius
# Specifying '-1' as the last paramter will fill the circle
cv2.circle(img, (304, 56), 10, (30, 45, 200), -1)

pts = np.array([[10, 50], [200, 30], [640, 50], [870, 100]])
#pts.reshape([-1, 1, 2])

# The true tells it to connect the last and the first point
cv2.polylines(img, [pts], True, (0, 45, 211), 3)

font = cv2.FONT_HERSHEY_SIMPLEX

# the last parameter 'LINE_AA' --> line antialiasing
# the last second '2' --> thickness of the text
cv2.putText(img, 'Apple!!', (350, 100), font, 1, (20, 30, 40), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
