#error!!!
import cv2

image1 = cv2.imread('Assests/water.jpeg')
image2 = cv2.imread('Assests/clouds.jpeg')

blend = cv2.addWeighted(image1, 0.7, image2, 0.3, 0)
cv2.imshow('blend', blend)
cv2.waitKey(0)
cv2.destroyAllWindows()
