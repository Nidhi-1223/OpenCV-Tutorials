import cv2
filename = 'Assests/road.jpg'
image_gray = cv2.imread(filename, 0)         #here 0 means we are reading the image in grayscale
image_rgb = cv2.imread(filename, 1)

cv2.imshow("title" ,image_gray)
cv2.imshow("title2", image_rgb)
# cv2.imwrite()

cv2.waitKey(0)          #waitKey(0) blocks the code indefinitely. it ends when the user presses any key on the keyboard in the image window
cv2.destroyAllWindows()         #destroys all the windows