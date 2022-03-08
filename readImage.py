import cv2
image = cv2.imread('Assests/road.jpg')
h, w = image.shape[:2]
print("height = {}, width = {}".format(h,w))        #prints the dimensions
cv2.imshow('road', image)                           #displays the image
cv2.waitKey(0)
cv2.destroyAllWindows()
