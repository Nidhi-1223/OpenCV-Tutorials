import cv2
filename = 'Assests/road.jpg'
image = cv2.imread(filename, 0)         #here 0 means we are reading the image in grayscale

cv2.imwrite("Assests/imagegray.jpg",image )

cv2.waitKey(0)
cv2.destroyAllWindows()