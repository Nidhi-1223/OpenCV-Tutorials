#double click on the canvas to get a circle

import cv2
from matplotlib.pyplot import draw
import numpy as np
img = np.zeros((512, 512, 3), np.uint8)
def draw_circle(event, x, y, flags, param):
    if(event == cv2.EVENT_LBUTTONDBLCLK):
        cv2.circle(img,(x,y), 50, (225, 0, 0), -1 )

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    key = cv2.waitKey(20)
    if (key == ord('q')):
        break

cv2.destroyAllWindows()