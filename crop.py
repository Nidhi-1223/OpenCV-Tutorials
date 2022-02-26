import cv2
filename = 'Assests/road.jpg'

image = cv2.imread(filename, 1)
lower_x = 50
upper_x = 500
lower_y = 50
upper_y = 500
cropped_image = image[lower_x:upper_x, lower_y:upper_y]   #x - 20 to 200 ; y - 50 to 250
cv2.imshow("cropped image", cropped_image)
cv2.imwrite("Assests/cropped_image.jpg", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()