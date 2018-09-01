import cv2
import numpy as np

# capture video from the first web cam
cap = cv2.VideoCapture(0)

while True:

    _, frame = cap.read()

    # conver to hsv --> hue, saturation, value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hsv range that should be shown change according to the set, set using trail and error
    lower_red = np.array([150, 120, 50])
    upper_red = np.array([180, 255, 150])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', res)

    # 5--> 5ms delay
    # if esc key is pressed it breaks out of while loop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
