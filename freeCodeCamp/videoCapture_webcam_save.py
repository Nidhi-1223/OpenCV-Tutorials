import numpy as np
import cv2

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Assests/output.avi', fourcc, 20.0, (640,480))

while(True):
    ret, frame = capture.read()
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    out.write(frame)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(100)
    print(key)

    if(key == ord('q')):     #if (key == 113)       its gonna quit when we press "q"
            break

capture.release()
out.release()
cv2.destroyAllWindows()
