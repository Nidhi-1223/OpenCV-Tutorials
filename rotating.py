import cv2
import numpy as np

FILE_NAME = 'Assests/water.jpeg'
try:
    image = cv2.imread(FILE_NAME)
    (rows, cols) = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2), 45,1)
    res = cv2.warpAffine(image , M, (cols, rows))
    cv2.imwrite('rotating.jpg', res)
    

except IOError:
    print("Error while reading files!")