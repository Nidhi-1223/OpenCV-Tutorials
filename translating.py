import cv2
import numpy as np

FILE_NAME = 'Assests/water.jpeg'
M = np.float32([[1,0,100], [0, 1, 50]])

try:
    image = cv2.imread(FILE_NAME)
    (rows, cols) = image.shape[:2]
    res = cv2.warpAffine(image, M, (cols,rows))
    cv2.imwrite('Assests/result_translated_photo.jpg', res)

except IOError:
    print("Error while reading files!")