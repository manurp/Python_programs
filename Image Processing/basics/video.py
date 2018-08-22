import cv2
import numpy as np

# capture video from webcam
# 0 --> primary camera
# 1 --> second camera
cap = cv2.VideoCapture(0)

# video codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# output video file
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# should release the capture and output video file
cap.release()
out.release()
cv2.destroyAllWindows()
