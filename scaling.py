import cv2
import numpy as np

FILE_NAME = 'Assests/water.jpeg'
try:
    image = cv2.imread(FILE_NAME)
    (height, width) = image.shape[:2]
    resized = cv2.resize(image, (int(width/2), int(height/2)), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('../Assests/scaled_image.jpg', resized)

except IOError:
    print("Error while reading files!")