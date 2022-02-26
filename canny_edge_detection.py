import cv2
import numpy as np

FILE_NAME = 'Assests/horse.jpeg'
try:
    image = cv2.imread(FILE_NAME)
    edges = cv2.Canny(image, 100, 200)
    cv2.imwrite('Assests/edgeDetection.jpg', edges)

except IOError:
    print('Error while reading files!')
