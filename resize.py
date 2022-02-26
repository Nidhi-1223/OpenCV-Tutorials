import cv2
filename = 'Assests/road.jpg'
image = cv2.imread(filename, 1)
resize = cv2.resize(image, (800, 800))
cv2.imshow("image", image)
cv2.imshow("resized", resize)
cv2.waitKey(0)
cv2.destroyAllWindows()