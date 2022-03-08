import numpy as np
import cv2
filename = 'Assests/horse.jpeg'

image = cv2.imread(filename)
cv2.circle(image, 
            (80,80),
            50,
            (255,0,0),
            -1)

cv2.imshow("idk man, it's late", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#for other shapes - https://www.javatpoint.com/opencv-drawing-functions